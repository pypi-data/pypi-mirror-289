# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
# pylint: disable=broad-exception-caught
from typing import Optional
from ipulse_shared_core_ftredge.enums.enums_cloud import CloudProvider
from .utils_cloud_gcp import (write_json_to_gcs_extended, read_json_from_gcs)

#######################################################################################################################
#######################################################################################################################
#################################################     cloud IO functions      ########################################

# Define the central function that routes to the relevant cloud-specific function
def write_json_to_cloud_storage_extended(cloud_provider:CloudProvider, storage_client, data:dict | list | str, bucket_name: str, file_name: str,
                      file_exists_if_starts_with_prefix:Optional[str] =None, overwrite_if_exists:bool=False, increment_if_exists:bool=False,
                      max_retries:int=2, max_deletable_files:int=1, logger=None, print_out=False):


    if cloud_provider == CloudProvider.GCP:
       return write_json_to_gcs_extended(
            storage_client=storage_client,
            data=data,
            bucket_name=bucket_name,
            file_name=file_name,
            file_exists_if_starts_with_prefix=file_exists_if_starts_with_prefix,
            overwrite_if_exists=overwrite_if_exists,
            increment_if_exists=increment_if_exists,
            max_retries=max_retries,
            max_deletable_files=max_deletable_files,
            logger=logger,
            print_out=print_out
        )

    raise ValueError(f"Unsupported cloud provider: {cloud_provider}. Supported cloud providers: gcp")


def read_json_from_cloud_storage(cloud_provider:CloudProvider, storage_client, bucket_name, file_name, logger=None, print_out=False):
    if cloud_provider == CloudProvider.GCP:
        return read_json_from_gcs(storage_client=storage_client, bucket_name=bucket_name, file_name=file_name, logger=logger, print_out=print_out)

    raise ValueError(f"Unsupported cloud provider: {cloud_provider}. Supported cloud providers: gcp")
