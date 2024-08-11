# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
# pylint: disable=broad-exception-raised
# from typing import Optional
# from ipulse_shared_core_ftredge.enums import DataSourceType
# from .utils_collector_pipelinemon import Pipelinemon
# from .utils_cloud_gcp import write_json_to_gcs_extended


# def write_json_to_cloud_storage_with_pipelinemon_extended(cloud_storage_type:DataSourceType, cloud_storage_client, pipelinemon:Pipelinemon,
#                                                            data:dict | list | str, bucket_name: str, file_name: str,
                                                            
                                                            
#                                                             max_retries:int=2, max_deletable_files:int=1):

#     supported_cloud_storage_types = [DataSourceType.GCS]
#     if cloud_storage_type == DataSourceType.GCS:
#         return write_json_to_gcs_extended(pipelinemon=pipelinemon, storage_client=cloud_storage_client, data=data, bucket_name=bucket_name, file_name=file_name,
#                                                   ,
#                                                   max_retries=max_retries,
#                                                   max_deletable_files=max_deletable_files)

#     raise ValueError(f"Unsupported cloud provider: {cloud_storage_type}. Supported cloud providers: {supported_cloud_storage_types}")
