# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
from enum import Enum


class DataPrimaryCategory(Enum):
    HISTORIC = "historic" # Historical data, usually accurate and complete
    HISTORIC_OPINION="histopinion" # Opinions and subjective data about the past, msotly unverified but recorded facts and ideas
    REAL_TIME="realtime" # Real-time data, not always certain, can have error
    ANALYTICS="analytics" # Analytical data and modelling, derived from historical and prediction data. Normally shall be making Human readable sense. vs. Features
    FEATURES="features" # Feature data, used for training models
    PREDICTIVE="predictive" # Predictive data, based on models and simulations

    SIMULATION_HISTORIC = "simhistoric" # Simulates past events
    SIMULATION_REAL_TIME = "simrealtime" #  Simulates live data streams
    SIMULATION_ANALYTICS = "simanalytics" #  Simulates live data streams
    SIMULATION_PREDICTIVE="simpredictive" # Simulated data, used for testing and training


class DataState(Enum):
    RAW = "raw" # Raw data, unprocessed, unverified
    FORMATTED= "formatted" # Formatted data
    CLEANED = "cleaned" # Cleaned data, of outliers and errors, filled
    PROCESSED = "processed" # Processed data, cleaned
    MODELED = "modeled" # Modeled data, processed and verified
    SIMULATED = "simulated" # Simulated data, processed and verified
    ANALYZED = "analyzed" # Analyzed data, processed and verified
    VERIFIED = "verified" # Verified data, separate category for data that has been verified. Perhaps Stock market prices cross checked between several sources

class DatasetPortionType(Enum):
    FULL_DATA= "full_data"
    PARTIAL_DATA= "partial_data"
    RECENT_LAST_DATA = "recent_last_data"
    RECENT_GAP_DATA = "recent_gap_data"

class DataSourceType(Enum):
    API = "api"
    WEBSITE = "website"
    LOCAL_STORAGE = "local_storage"
    INMEMORY = "inmemory"
    GCS = "gcs"
    DB = "db"
    BQ = "bq"
    FIREBASE = "firebase"
    MONGODB = "mongodb"
    PUBSUB = "pubsub"
    REDIS = "redis"
    S3 = "s3"
    AZURE_BLOB = "azure_blob"
    WEBSOCKET = "websocket"
    KAFKA = "kafka"
    ELASTICSEARCH = "elasticsearch"
    CASSANDRA = "cassandra"
    DYNAMODB = "dynamodb"
    MEMSQL = "memsql"
    ORACLE = "oracle"
    POSTGRESQL = "postgresql"
    SQLSERVER = "sqlserver"
    MYSQL = "mysql"

class PipelineTriggerType(Enum):
    MANUAL = "manual"
    SCHEDULED_RECENT = "scheduled_recent"
    SCHEDULED_VERIFICATION = "scheduled_verification"
    EVENT_GCS_UPLOAD= "event_gcs_upload"
    EVENT_PUBSUB= "event_pubsub"
    INSIDE_FUNCTION = "inside_function"

class ExecutionLocation(Enum):
    LOCAL_SCRIPT = "local_script"
    LOCAL_JUPYTER_NOTEBOOK = "local_jupyter_notebook"
    CLOUD_JUPYTER = "cloud_jupyter_notebook"
    LOCAL_CF_EVENT_HTTP = "local_cf_event_http"
    CLOUD_CF_EVENT_HTTP = "cloud_cf_event_http"
    LOCAL_CF_EVENT_PUBSUB = "local_cf_event_pubsub"
    CLOUD_CF_EVENT_PUBSUB = "cloud_cf_event_pubsub"
    LOCAL_CF_EVENT_GCS = "local_cf_event_gcs"
    CLOUD_CF_EVENT_GCS = "cloud_cf_event_gcs"
    LOCAL_CF_EVENT_DB = "local_cf_event_db"
    CLOUD_CF_EVENT_DB = "cloud_cf_event_db"

class DataEventType(Enum):
    INSERT_NOREPLACE_1O_NT = "insert_noreplace_1o_nt"
    MERGE_NOREPLACE_NO_1T = "merge_noreplace_no_1t"
    MERGE_NOREPLACE_NO_NT = "merge_noreplace_no_nt"
    INSERT_NOREPLACE_1O_1T = "insert_noreplace_1o_1t"
    MERGE_NOREPLACE_1O_NT = "merge_noreplace_1o_nt"
    INSERT_REPLACE_1O_1T = "insert_replace_1o_1t"
    INSERT_REPLACE_1O_NT = "insert_replace_1o_nt"
    MERGE_REPLACE_NO_NT = "merge_replace_no_nt"
    MERGE_REPLACE_1O_NT = "merge_replace_1o_nt"
    MERGE_REPLACE_NO_1T = "merge_replace_no_1t"
    DELETE_1O_1T = "delete_1o_1t"
    DELETE_1O_NT = "delete_1o_nt"
    DELETE_NO_1T = "delete_no_1t"
    DELETE_NO_NT = "delete_no_nt"



class ComputeType(Enum):
    CPU= "cpu"
    GPU= "gpu"
    SPARK= "spark"
    TPU= "tpu"
    FPGA= "fpga"
    ASIC= "asic"
    QUANTUM= "quantum"
    HADOOP= "hadoop"
