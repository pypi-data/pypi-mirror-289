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
from typing import List, Union
from ipulse_shared_core_ftredge.enums import LoggingHandlers
from ipulse_shared_core_ftredge.utils.utils_cloud_gcp import add_gcp_cloud_logging, add_gcp_error_reporting

###################################################################################################
##################################################################################################
##################################### SETTING UP LOGGER ##########################################

class CloudLogFormatter(logging.Formatter):
    """Formats log records as structured JSON."""

    def format(self, record):
        log_entry = {
            'message': record.msg,
            'timestamp': self.formatTime(record, self.datefmt),
            'name': record.name,
            'severity': record.levelname,
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
        
        # Format log messages differently based on the log level
        if record.levelno == logging.INFO:
            log_message = f"[INFO] {self.formatTime(record, self.datefmt)} :: {record.msg}"
        elif record.levelno == logging.DEBUG:
            log_message = f"[DEBUG] {self.formatTime(record, self.datefmt)} :: {record.msg} :: {short_path} :: lineno {record.lineno} :: {record.name}"
        elif record.levelno == logging.ERROR:
            log_message = f"[ERROR] {self.formatTime(record, self.datefmt)} :: {record.msg} :: {short_path} :: lineno {record.lineno} :: {record.name}"
            if record.exc_info:
                log_message += "\n" + ''.join(traceback.format_exception(*record.exc_info))
        else:
            log_message = f"[{record.levelname}] {self.formatTime(record, self.datefmt)} :: {record.msg} :: {short_path} :: lineno {record.lineno} :: {record.name}"


        return log_message


def get_logger( logger_name:str ,level=logging.INFO, logging_handler_providers: Union[LoggingHandlers, List[LoggingHandlers]] = LoggingHandlers.NONE):

    """Creates and configures a logger with the specified handlers."""

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    cloud_formatter = CloudLogFormatter()

    # Ensure logging_handler_providers is a list for consistent processing
    if not isinstance(logging_handler_providers, list):
        logging_handler_providers = [logging_handler_providers]

    supported_remote_handlers = [
        LoggingHandlers.GCP_CLOUD_LOGGING,
        LoggingHandlers.GCP_ERROR_REPORTING,
        LoggingHandlers.LOCAL_STREAM,
        LoggingHandlers.NONE, # If NONE is considered a remote handler
    ]

    # Remote handlers

    for handler_provider in logging_handler_providers:
        if handler_provider in supported_remote_handlers:
            if handler_provider == LoggingHandlers.GCP_CLOUD_LOGGING:
                add_gcp_cloud_logging(logger, cloud_formatter)
            elif handler_provider == LoggingHandlers.GCP_ERROR_REPORTING:
                add_gcp_error_reporting(logger)
            elif handler_provider == LoggingHandlers.LOCAL_STREAM:  # Handle local stream
                local_handler = logging.StreamHandler()
                local_handler.setFormatter(LocalLogFormatter())
                logger.addHandler(local_handler)
        else:
            raise ValueError(
            f"Unsupported logging provider: {handler_provider}. "
            f"Supported providers: {[h.value for h in supported_remote_handlers]}"
            )
    return logger
