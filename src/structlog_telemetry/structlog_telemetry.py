import structlog
from .singleton_base import Singleton
import logging
import os


class StructLogTelemetry(Singleton):
    __app_name = None
    __app_version = None
    __logger = None
    __is_initialized = False

    def __init__(self, app_name, app_version, print_banner=True) -> None:
        if not self.__is_initialized:
            StructLogTelemetry.__app_name = app_name
            StructLogTelemetry.__app_version = app_version
            log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO").upper())
            structlog.configure(
                wrapper_class=structlog.make_filtering_bound_logger(log_level)
            )

            StructLogTelemetry.__logger = structlog.get_logger(app_name)
            self.__is_initialized = True
            if print_banner:
                self.print_banner()

    def print_banner(self):
        print(f"{self.__app_name} 📟 {self.__app_version}")

    def set_process_id(_, __, event_dict):
        event_dict["process_id"] = os.getpid()
        return event_dict

    def configure_json_renderer():
        structlog.configure(
            processors=[
                structlog.processors.add_log_level,
                structlog.processors.TimeStamper(fmt="iso"),
                StructLogTelemetry.set_process_id,
                structlog.processors.JSONRenderer(),
            ]
        )


    def debug(self, value):
        self.__logger.debug(value)

    def info(self, value):
        self.__logger.info(value)

    def warning(self, value):
        self.__logger.warning(value)

    def error(self, value):
        self.__logger.error(value)

    def exception(self, value):
        self.__logger.exception(value)

    def critical(self, value):
        self.__logger.critical(value)


