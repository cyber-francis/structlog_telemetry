from src.structlog_telemetry.structured_logger import StructuredLogger


def test_structured_logger():
    logger = StructuredLogger(app_name="simple_logger", app_version="v0.0.1")
    logger.debug({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})
    logger.info({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})
    logger.warning({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})
    logger.error({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})
    logger.exception({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})
    logger.critical({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})
