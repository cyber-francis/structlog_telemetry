import structlog
from .singleton_base import Singleton
import logging
import os


class StructuredLogger(Singleton):
    __app_name = None
    __app_version = None
    __log_name = None
    __logger = None

    def __init__(self, app_name, app_version, json_renderer=False) -> None:
        # configure structlog to output structured log in JSON format
        StructuredLogger.__app_name = app_name
        StructuredLogger.__app_version = app_version
        StructuredLogger.__log_name = app_name
        StructuredLogger.__json_renderer = json_renderer
        log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO").upper())
        structlog.configure(
            wrapper_class=structlog.make_filtering_bound_logger(log_level)
        )
        if StructuredLogger.__json_renderer:
            StructuredLogger.configure_json_renderer()

        StructuredLogger.__logger = structlog.get_logger(app_name)

    def set_process_id(_, __, event_dict):
        event_dict["process_id"] = os.getpid()
        return event_dict

    def configure_json_renderer():
        structlog.configure(
            processors=[
                structlog.processors.add_log_level,
                structlog.processors.TimeStamper(fmt="iso"),
                StructuredLogger.set_process_id,
                structlog.processors.JSONRenderer(),
            ]
        )

    def create_kv(self, *args):
        if StructuredLogger.__json_renderer:
            return {
                "app_name": self.__app_name,
                "app_version": self.__app_version,
                "event": args[0][0],
            }
        else:
            return {
                "app_name": self.__app_name,
                "app_version": self.__app_version,
                "details": args[0][0],
            }

    def debug(self, *args):
        self.__logger.debug(self.create_kv(args))

    def info(self, *args):
        self.__logger.info(self.create_kv(args))

    def warning(self, *args):
        self.__logger.warning(self.create_kv(args))

    def error(self, *args):
        self.__logger.error(self.create_kv(args))

    def exception(self, *args):
        self.__logger.exception(self.create_kv(args))

    def critical(self, *args):
        self.__logger.critical(self.create_kv(args))
