# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
# pylint: disable=broad-exception-raised

# import json
# import os
# import time
# from google.cloud.storage import Client as GCSClient
# from ipulse_shared_core_ftredge.enums import LogLevel, DuplicationHandling, DuplicationHandlingStatus, MatchConditionType, DataSourceType
# from ipulse_shared_core_ftredge.utils import log_error, log_info
# from .utils_collector_pipelinemon import Pipelinemon
# from .logs.context_log import ContextLog





# def write_json_to_gcs_with_pipelinemon_extended( pipelinemon:Pipelinemon, storage_client:GCSClient, data:dict | list | str, bucket_name: str, file_name: str,
#                       file_exists_if_starts_with_prefix:Optional[str] =None, overwrite_if_exists:bool=False, increment_if_exists:bool=False,
#                       max_retries:int=2, max_deletable_files:int=1):
#     """Saves data to Google Cloud Storage and optionally locally.
    
#     This function attempts to upload data to GCS. 
#     - If the upload fails after retries and `save_locally` is True or `local_path` is provided, it attempts to save the data locally.
#     - It handles file name conflicts based on these rules:
#         - If `overwrite_if_exists` is True: 
#             - If `file_exists_if_contains_substr` is provided, ANY existing file containing the substring is deleted, and the new file is saved with the provided `file_name`.
#             - If `file_exists_if_contains_substr` is None, and a file with the exact `file_name` exists, it's overwritten.
#         - If `increment_if_exists` is True:
#             - If `file_exists_if_contains_substr` is provided, a new file with an incremented version is created ONLY if a file with the EXACT `file_name` exists.
#             - If `file_exists_if_contains_substr` is None, a new file with an incremented version is created if a file with the exact `file_name` exists. 
            
#         -If both overwrite_if_exists and increment_if_exists are provided as Ture, an exception will be raised.
#     """

#     cloud_storage_ref="GCP_GCS"

#     with pipelinemon.context(f"write_json_to_{cloud_storage_ref}_with_pipelinemon"):
#         cloud_storage_upload_error = None
#         # Input validation
#         if overwrite_if_exists and increment_if_exists:
#             err_msg="Both 'overwrite_if_exists' and 'increment_if_exists' cannot be True simultaneously."
#             pipelinemon.add_log(ContextLog(LogLevel.ERROR_CUSTOM, subject="Param validation", description=err_msg))
#             return {"cloud_storage_upload_error": err_msg}
#         if max_deletable_files > 10:
#             err_msg="max_deletable_files should be less than 10 for safety. For more use another method."
#             pipelinemon.add_log(ContextLog(LogLevel.ERROR_CUSTOM,subject="max_deletable_files", description=err_msg))
#             return {"cloud_storage_upload_error": err_msg}

#         # Prepare data
#         if isinstance(data, (list, dict)):
#             data_str = json.dumps(data, indent=2)
#         else:
#             data_str = data

#         bucket = storage_client.bucket(bucket_name)
#         base_file_name, ext = os.path.splitext(file_name)
#         increment = 0
#         attempts = 0
#         success = False

#         # GCS-related metadata
#         cloud_storage_path = None
#         cloud_storage_file_overwritten = False
#         cloud_storage_file_already_exists = False
#         cloud_storage_file_saved_with_increment = False
#         cloud_storage_file_exists_checked_on_name = file_name
#         cloud_storage_deleted_files=[]

#         try:
#             upload_allowed = True
#             # --- Overwrite Logic ---
#             if overwrite_if_exists:
#                 with pipelinemon.context("overwriting"):
#                     if file_exists_if_starts_with_prefix:
#                         cloud_storage_file_exists_checked_on_name = file_exists_if_starts_with_prefix
#                         blobs_to_delete = list(bucket.list_blobs(prefix=file_exists_if_starts_with_prefix))
#                         if len(blobs_to_delete) > max_deletable_files:
#                             err_msg=f"Error: Attempt to delete {len(blobs_to_delete)} matched files, but limit is {max_deletable_files}."
#                             pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_exists_if_starts_with_prefix, description=f"Prefix matched with {len(blobs_to_delete)} files in bucket {bucket_name}"))
#                             pipelinemon.add_log(ContextLog(LogLevel.ERROR_CUSTOM, subject="Too many files", description=err_msg))
#                             #### Ensuring to quit the operation if too many files are found, it will be catched below
#                             return {"cloud_storage_upload_error": err_msg}
#                         if blobs_to_delete:
#                             cloud_storage_file_already_exists = True
#                             pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_exists_if_starts_with_prefix, description=f"Prefix matched with {len(blobs_to_delete)} files in bucket {bucket_name}"))
#                             for blob in blobs_to_delete:
#                                 cloud_storage_path_del = f"gs://{bucket_name}/{blob.name}"
#                                 pipelinemon.add_system_impacted(f"delete: {cloud_storage_ref}_bucket_file: {cloud_storage_path_del}")
#                                 blob.delete()
#                                 pipelinemon.add_log(ContextLog(LogLevel.INFO_REMOTE_DELETE_COMPLETE, subject= cloud_storage_path_del, description=f"file deleted from {cloud_storage_ref} as part of overwrite, matched with prefix"))
#                                 cloud_storage_deleted_files.append(cloud_storage_path_del)
#                             cloud_storage_file_overwritten = True
#                     elif bucket.blob(file_name).exists():
#                         cloud_storage_file_already_exists = True
#                         pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_name, description=f"Exact name matched with existing file in bucket {bucket_name}"))
#                         cloud_storage_path_del = f"gs://{bucket_name}/{file_name}"
#                         pipelinemon.add_system_impacted(f"delete: {cloud_storage_ref}_bucket_file: {cloud_storage_path_del}")
#                         blob.delete()  # Delete the existing blob
#                         pipelinemon.add_log(ContextLog(LogLevel.INFO_REMOTE_DELETE_COMPLETE, subject= cloud_storage_path_del, description=f"file deleted from {cloud_storage_ref} as part of overwrite, matched with exact name"))
#                         cloud_storage_deleted_files.append(cloud_storage_path_del)
#                         cloud_storage_file_overwritten = True
#             # --- Increment Logic ---
#             elif increment_if_exists:
#                 with pipelinemon.context("incrementing"):
#                     cloud_storage_file_exists_checked_on_name = file_name  # We only increment if the exact name exists
#                     while bucket.blob(file_name).exists():
#                         cloud_storage_file_already_exists = True
#                         increment += 1
#                         file_name = f"{base_file_name}_v{increment}{ext}"
#                         cloud_storage_file_saved_with_increment = True
#                     if increment>0:
#                         cloud_storage_path = f"gs://{bucket_name}/{file_name}"
#                         pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_name, description=f"Attempting to save file with incremented version in {bucket_name}"))
#              # --- Check for Conflicts (Including Prefix) ---
#             else:
#                 if file_exists_if_starts_with_prefix:
#                     blobs_matched = list(bucket.list_blobs(prefix=file_exists_if_starts_with_prefix))
#                     cloud_storage_file_exists_checked_on_name = file_exists_if_starts_with_prefix
#                     if blobs_matched:
#                         upload_allowed = False
#                         cloud_storage_file_already_exists = True
#                         pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_exists_if_starts_with_prefix, description=f"Prefix matched with {len(blobs_matched)} existing files in bucket {bucket_name}."))
#                 elif bucket.blob(file_name).exists():
#                     pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_name, description=f"Exact name matched with existing file in bucket {bucket_name}."))
#                     upload_allowed = False
#                     cloud_storage_file_already_exists = True

#             # --- GCS Upload ---
#             cloud_storage_path = f"gs://{bucket_name}/{file_name}"
#             if overwrite_if_exists or increment_if_exists or upload_allowed:
#                 with pipelinemon.context("uploading"):
#                     while attempts < max_retries and not success:
#                         try:
#                             blob = bucket.blob(file_name)  # Use the potentially updated file_name
#                             pipelinemon.add_system_impacted(f"upload: {cloud_storage_ref}_bucket_file: {cloud_storage_path}")
#                             blob.upload_from_string(data_str, content_type='application/json')
#                             pipelinemon.add_log(ContextLog(LogLevel.INFO_REMOTE_PERSISTNACE_COMPLETE, subject= cloud_storage_path, description=f"file uploaded to {cloud_storage_ref}"))
#                             success = True
#                         except Exception as e:
#                             attempts += 1
#                             if attempts < max_retries:
#                                 time.sleep(2 ** attempts)
#                             else:
#                                 err_msg=f"Error uploading file to {cloud_storage_ref} bucket {bucket_name} with name {file_name} : {type(e).__name__}-{str(e)}"
#                                 pipelinemon.add_log(ContextLog(LogLevel.ERROR_EXCEPTION, e=e, description=err_msg))
#                                 return {"cloud_storage_upload_error": err_msg}

#         except Exception as e:
#             pipelinemon.add_log(ContextLog(LogLevel.ERROR_EXCEPTION, e=e))
#             return {"cloud_storage_upload_error": f"Exception in GCS upload {type(e).__name__}-{str(e)}"}
#     # --- Return Metadata ---
#     return {
#         "cloud_storage_path": cloud_storage_path if ((success or not upload_allowed) and not cloud_storage_upload_error ) else None,
#         "cloud_storage_file_already_exists": cloud_storage_file_already_exists,
#         "cloud_storage_file_exists_checked_on_name":cloud_storage_file_exists_checked_on_name ,
#         "cloud_storage_file_overwritten": cloud_storage_file_overwritten,
#         "cloud_storage_deleted_file_names": ",,,".join(cloud_storage_deleted_files) if cloud_storage_deleted_files else None,
#         "cloud_storage_file_saved_with_increment": cloud_storage_file_saved_with_increment,
#         "cloud_storage_upload_error": cloud_storage_upload_error
#     }

