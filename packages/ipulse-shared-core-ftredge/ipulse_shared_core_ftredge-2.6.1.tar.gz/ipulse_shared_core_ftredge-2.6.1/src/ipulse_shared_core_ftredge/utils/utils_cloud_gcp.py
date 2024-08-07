# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
# pylint: disable=broad-exception-raised
import json
import csv
from io import StringIO
import os
import time
import logging
from typing import Optional
import traceback
from google.api_core.exceptions import NotFound
from google.cloud import error_reporting
from google.cloud import logging as cloud_logging
from google.cloud.storage import Client as GCSClient
from google.cloud import bigquery

############################################################################
##################### GOOGLE CLOUD  UTILS ##################################
############################################################################

def log_error(message, logger=None , print_out=False, exc_info=False):
    if logger:
        logger.error(message, exc_info=exc_info)
    elif print_out:
        print(message)

def log_warning(message, logger=None, print_out=False):
    if logger:
        logger.warning(message)
    elif print_out:
        print(message)

def log_info(message, logger=None, print_out=False):
    if logger:
        logger.info(message)
    elif print_out:
        print(message)



############################################################################
##################### LOGGING and ERROR reporting ##########################
####DEPCREACATED: THIS APPROACH WAS GOOD, BUT ERRORS WERE NOT REPORTED TO ERROR REPORTING
# logging.basicConfig(level=logging.INFO)
# logging_client = google.cloud.logging.Client()
# logging_client.setup_logging()
###################################
def setup_gcp_logging(logger, formatter, enable_error_reporting=True):

    class CustomGCPErrorReportingHandler(logging.Handler):
        def __init__(self, level=logging.ERROR):
            super().__init__(level)
            self.error_client = error_reporting.Client()
            self.propagate = True

        def emit(self, record):
            try:
                if record.levelno >= logging.ERROR:
                    log_struct = {
                    'message': self.format(record),
                    'severity': record.levelname,
                    'pathname': getattr(record, 'pathname', None),
                    'lineno': getattr(record, 'lineno', None)
                }
                if record.exc_info:
                    log_struct['exception'] = ''.join(
                        traceback.format_exception(*record.exc_info)
                    )
                self.error_client.report(str(log_struct))
            except Exception as e:
                self.handleError(record)
        
    class CustomGCPLoggingHandler(cloud_logging.handlers.CloudLoggingHandler):
        """Custom handler for Google Cloud Logging with a dynamic logName."""
        def __init__(self, client, name, resource=None, labels=None):
            super().__init__(client=client, name=name, resource=resource, labels=labels)
            
        def emit(self, record):
            # 1. Create the basic log entry dictionary
            log_entry = {
                'message': record.msg,
                'severity': record.levelname,
                'name': record.name,
                'pathname': record.filename,
                'lineno': record.lineno,
            }
            if record.exc_info:
                log_entry['exception_traceback'] = ''.join(
                    traceback.format_exception(*record.exc_info)
                )

            # 2. Apply the formatter to the 'message' field if it's a dictionary
            if isinstance(record.msg, dict):
                formatted_message = self.formatter.format(record)
                try:
                    log_entry['message'] = json.loads(formatted_message)
                except json.JSONDecodeError:
                    log_entry['message'] = formatted_message
            else:
                log_entry['message'] = record.msg

            # 3. Set the custom logName
            log_entry['logName'] = f"projects/{self.client.project}/logs/{record.name}"

            # 4. Send to Google Cloud Logging
            super().emit(record)

    # Create Google Cloud Logging handler
    cloud_logging_client = cloud_logging.Client()
    cloud_logging_handler = CustomGCPLoggingHandler(cloud_logging_client, logger.name)  # No prefix needed
    cloud_logging_handler.setFormatter(formatter)
    logger.addHandler(cloud_logging_handler)

    if enable_error_reporting:
        # Create and add Error Reporting handler
        error_reporting_handler = CustomGCPErrorReportingHandler()
        logger.addHandler(error_reporting_handler)



def create_bigquery_schema_from_json(json_schema: list) -> list:
    schema = []
    for field in json_schema:
        if "max_length" in field:
            schema.append(bigquery.SchemaField(field["name"], field["type"], mode=field["mode"], max_length=field["max_length"]))
        else:
            schema.append(bigquery.SchemaField(field["name"], field["type"], mode=field["mode"]))
    return schema


def read_json_from_gcs(storage_client:GCSClient, bucket_name:str, file_name:str, logger=None,print_out=False):
    """ Helper function to read a JSON file from Google Cloud Storage """
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data_string = blob.download_as_text()
        data = json.loads(data_string)
        return data
    except NotFound:
        log_error(message=f"Error: The file {file_name} was not found in the bucket {bucket_name}.", logger=logger, print_out=print_out)
        return None
    except json.JSONDecodeError:
        log_error(message=f"Error: The file {file_name} could not be decoded as JSON.", logger=logger, print_out=print_out)
        return None
    except Exception as e:
        log_error(message=f"An unexpected error occurred: {e}", exc_info=True, logger=logger, print_out=print_out)
        return None

def read_csv_from_gcs(bucket_name:str, file_name:str, storage_client:GCSClient, logger=None, print_out=False):
    """ Helper function to read a CSV file from Google Cloud Storage """

    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data_string = blob.download_as_text()
        data_file = StringIO(data_string)
        reader = csv.DictReader(data_file)
        return list(reader)
    except NotFound:
        log_error(message=f"Error: The file {file_name} was not found in the bucket {bucket_name}.", logger=logger, print_out=print_out)
        return None
    except csv.Error:
        log_error(message=f"Error: The file {file_name} could not be read as CSV.", logger=logger, print_out=print_out)
        return None
    except Exception as e:
        log_error(message=f"An unexpected error occurred: {e}", logger=logger, print_out=print_out, exc_info=True)
        return None



def write_json_to_gcs_extended( storage_client:GCSClient, data:dict | list | str, bucket_name: str, file_name: str,
                      file_exists_if_starts_with_prefix:Optional[str] =None, overwrite_if_exists:bool=False, increment_if_exists:bool=False,
                      max_retries:int=2, max_deletable_files:int=1, logger=None, print_out=False):
    
    """Saves data to Google Cloud Storage and optionally locally.
    
    This function attempts to upload data to GCS. 
    - If the upload fails after retries and `save_locally` is True or `local_path` is provided, it attempts to save the data locally.
    - It handles file name conflicts based on these rules:
        - If `overwrite_if_exists` is True: 
            - If `file_exists_if_contains_substr` is provided, ANY existing file containing the substring is deleted, and the new file is saved with the provided `file_name`.
            - If `file_exists_if_contains_substr` is None, and a file with the exact `file_name` exists, it's overwritten.
        - If `increment_if_exists` is True:
            - If `file_exists_if_contains_substr` is provided, a new file with an incremented version is created ONLY if a file with the EXACT `file_name` exists.
            - If `file_exists_if_contains_substr` is None, a new file with an incremented version is created if a file with the exact `file_name` exists. 
            
        -If both overwrite_if_exists and increment_if_exists are provided as Ture, an exception will be raised.
    """
    # GCS upload exception
    # Input validation
    if overwrite_if_exists and increment_if_exists:
        raise ValueError("Both 'overwrite_if_exists' and 'increment_if_exists' cannot be True simultaneously.")
    if not isinstance(data, (list, dict, str)):
        raise ValueError("Data should be a list, dict, or string.")
    if max_deletable_files > 10:
        raise ValueError("max_deletable_files should be less than 10 for safety. For more use another method.")

    # Prepare data
    if isinstance(data, (list, dict)):
        data_str = json.dumps(data, indent=2)
    else:
        data_str = data

    bucket = storage_client.bucket(bucket_name)
    base_file_name, ext = os.path.splitext(file_name)
    increment = 0
    attempts = 0
    success = False

    # GCS-related metadata
    cloud_storage_path = None
    cloud_storage_file_overwritten = False
    cloud_storage_file_already_exists = False
    cloud_storage_file_saved_with_increment = False
    cloud_storage_file_exists_checked_on_name = file_name
    cloud_storage_deleted_files=[]

    
    upload_allowed = True
    # --- Overwrite Logic ---
    if overwrite_if_exists:
        if file_exists_if_starts_with_prefix:
            cloud_storage_file_exists_checked_on_name = file_exists_if_starts_with_prefix
            blobs_to_delete = list(bucket.list_blobs(prefix=file_exists_if_starts_with_prefix))
            if len(blobs_to_delete) > max_deletable_files:
                raise Exception(f"Error: Attempt to delete {len(blobs_to_delete)} matched files, but limit is {max_deletable_files}.")
            if blobs_to_delete:
                for blob in blobs_to_delete:
                    cloud_storage_path_del = f"gs://{bucket_name}/{blob.name}"
                    blob.delete()
                    cloud_storage_deleted_files.append(cloud_storage_path_del)
                cloud_storage_file_overwritten = True
        elif bucket.blob(file_name).exists():
            cloud_storage_file_already_exists = True
            cloud_storage_path_del = f"gs://{bucket_name}/{file_name}"
            blob.delete()  # Delete the existing blob
            cloud_storage_deleted_files.append(cloud_storage_path_del)
            cloud_storage_file_overwritten = True
    # --- Increment Logic ---
    elif increment_if_exists:
        cloud_storage_file_exists_checked_on_name = file_name  # We only increment if the exact name exists
        while bucket.blob(file_name).exists():
            cloud_storage_file_already_exists = True
            increment += 1
            file_name = f"{base_file_name}_v{increment}{ext}"
            cloud_storage_file_saved_with_increment = True
        if increment>0:
            cloud_storage_path = f"gs://{bucket_name}/{file_name}"
        # --- Check for Conflicts (Including Prefix) ---
    else:
        if file_exists_if_starts_with_prefix:
            blobs_matched = list(bucket.list_blobs(prefix=file_exists_if_starts_with_prefix))
            cloud_storage_file_exists_checked_on_name = file_exists_if_starts_with_prefix
            if blobs_matched:
                upload_allowed = False
                cloud_storage_file_already_exists = True
        elif bucket.blob(file_name).exists():
            upload_allowed = False
            cloud_storage_file_already_exists = True

    # --- GCS Upload ---
    cloud_storage_path = f"gs://{bucket_name}/{file_name}"
    if overwrite_if_exists or increment_if_exists or upload_allowed:
        while attempts < max_retries and not success:
            try:
                blob = bucket.blob(file_name)  # Use the potentially updated file_name
                blob.upload_from_string(data_str, content_type='application/json')
                success = True
            except Exception as e:
                attempts += 1
                if attempts < max_retries:
                    time.sleep(2 ** attempts)
                else:
                    raise e

    # --- Return Metadata ---
    return {
        "cloud_storage_path": cloud_storage_path if (success or not upload_allowed ) else None,
        "cloud_storage_file_already_exists": cloud_storage_file_already_exists,
        "cloud_storage_file_exists_checked_on_name":cloud_storage_file_exists_checked_on_name ,
        "cloud_storage_file_overwritten": cloud_storage_file_overwritten,
        "cloud_storage_deleted_file_names": ",,,".join(cloud_storage_deleted_files) if cloud_storage_deleted_files else None,
        "cloud_storage_file_saved_with_increment": cloud_storage_file_saved_with_increment
    }


def write_csv_to_gcs(bucket_name:str, file_name:str, data:dict | list | str, storage_client:GCSClient, logger,log_info_verbose=True):
    """ Helper function to write a CSV file to Google Cloud Storage """
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data_file = StringIO()
        if data and isinstance(data, list) and isinstance(data[0], dict):
            fieldnames = data[0].keys()
            writer = csv.DictWriter(data_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        else:
            raise ValueError("Data should be a list of dictionaries")
        blob.upload_from_string(data_file.getvalue(), content_type='text/csv')
        if log_info_verbose:
            logger.info(f"Successfully wrote CSV to {file_name} in bucket {bucket_name}.")
    except ValueError as e:
        logger.error(f"ValueError: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while writing CSV to GCS: {e}", exc_info=True)
