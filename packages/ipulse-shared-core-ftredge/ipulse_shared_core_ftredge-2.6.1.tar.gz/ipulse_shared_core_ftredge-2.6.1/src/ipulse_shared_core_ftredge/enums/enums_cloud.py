
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

from enum import Enum


class CloudProvider(Enum):
    GCP = "gcp"
    AWS = "aws"
    AZURE = "azure"
    NO_CLOUD = "no_cloud"
    CLOUD_AGNOSTIC = "cloud_agnostic"
    OTHER = "other"
    UNKNWON = "unknown"
