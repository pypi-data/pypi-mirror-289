# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
# pylint: disable=broad-exception-raised
from typing import Optional
from ipulse_shared_core_ftredge.enums.enums_cloud import CloudProvider
from .utils_collector_pipelinemon import Pipelinemon
from .utils_cloud_gcp_with_collectors import write_json_to_gcs_with_pipelinemon_extended


def write_json_to_cloud_storage_with_pipelinemon_extended(cloud_provider:CloudProvider, pipelinemon:Pipelinemon, storage_client, data:dict | list | str, bucket_name: str, file_name: str,
                      file_exists_if_starts_with_prefix:Optional[str] =None, overwrite_if_exists:bool=False, increment_if_exists:bool=False,
                      max_retries:int=2, max_deletable_files:int=1):


    if cloud_provider == CloudProvider.GCP:
        return write_json_to_gcs_with_pipelinemon_extended(pipelinemon=pipelinemon, storage_client=storage_client, data=data, bucket_name=bucket_name, file_name=file_name,
                                                  file_exists_if_starts_with_prefix=file_exists_if_starts_with_prefix,
                                                  overwrite_if_exists=overwrite_if_exists, increment_if_exists=increment_if_exists,
                                                  max_retries=max_retries,
                                                  max_deletable_files=max_deletable_files)

    raise ValueError(f"Unsupported cloud provider: {cloud_provider}. Supported cloud providers: {CloudProvider.GCP.value}")
