# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
# pylint: disable=broad-exception-raised
import logging
import os
import json
import traceback
from ipulse_shared_core_ftredge.enums.enums_cloud import CloudProvider
from ipulse_shared_core_ftredge.utils.utils_cloud_gcp import setup_gcp_logging

###################################################################################################
##################################################################################################
##################################### SETTING UP LOGGER ##########################################

class CloudLogFormatter(logging.Formatter):
    """Formats log records as structured JSON."""

    def format(self, record):
        log_entry = {
            'timestamp': self.formatTime(record, self.datefmt),
            'name': record.name,
            'severity': record.levelname,
            'message': record.msg,
            'pathname': record.pathname,
            'lineno': record.lineno,
        }
        if record.exc_info:
            log_entry['exception_traceback'] = ''.join(traceback.format_exception(*record.exc_info))
        if isinstance(record.msg, dict):
            log_entry.update(record.msg)
        return json.dumps(log_entry)


class LocalLogFormatter(logging.Formatter):
    """Formats log records for local output to the console."""

    def format(self, record):  # Make sure you have the 'record' argument here!
        path_parts = record.pathname.split(os.sep)
        
        # Get the last two parts of the path if they exist
        if len(path_parts) >= 2:
            short_path = os.path.join(path_parts[-2], path_parts[-1])
        else:
            short_path = record.pathname

        log_message = f"{record.levelname} ::: {record.name} ::: {short_path} ::: lineno: {record.lineno} ::: {self.formatTime(record, self.datefmt)} ::: message: {record.msg}"
        if record.exc_info:
            log_message += "\n" + ''.join(
                traceback.format_exception(*record.exc_info)
            )
        return log_message


def get_logger( logger_name:str ,level=logging.INFO,  enable_local_streamer=False, cloud_provider:CloudProvider=CloudProvider.NO_CLOUD,  enable_error_reporting=True ):

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    cloud_formatter = CloudLogFormatter()

    without_cloud_logging_handler = [CloudProvider.NO_CLOUD, CloudProvider.CLOUD_AGNOSTIC, CloudProvider.UNKNWON, CloudProvider.OTHER]

    if cloud_provider in without_cloud_logging_handler or enable_local_streamer:
        handler = logging.StreamHandler()
        handler.setFormatter(LocalLogFormatter())
        logger.addHandler(handler)

    if cloud_provider == CloudProvider.GCP:
        setup_gcp_logging(logger=logger, formatter=cloud_formatter, enable_error_reporting=enable_error_reporting)
    elif  cloud_provider not in without_cloud_logging_handler:
        raise ValueError(f"Unsupported cloud provider: {cloud_provider}. Supported cloud providers: {CloudProvider.GCP.value}")

    return logger