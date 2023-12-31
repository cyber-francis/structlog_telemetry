import structlog
from singleton_base import Singleton
import logging
import os

class StructuredLogger(Singleton):
    __app_name = None
    __app_version = None
    __log_name = None
    __logger = None

    def __init__(self, app_name, app_version) -> None:
        # configure structlog to output structured log in JSON format
        StructuredLogger.__app_name = app_name
        StructuredLogger.__app_version = app_version
        StructuredLogger.__log_name = app_name
        log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO").upper())
        structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(log_level))
        StructuredLogger.__logger = structlog.get_logger(app_name)


    def create_kv(self, *args):
        return {"APP_NAME": self.__app_name, "APP_VERSION": self.__app_version, "EVENT": args[0][0]}
    

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