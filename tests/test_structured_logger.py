from src.structlog_telemetry.structured_logger import StructuredLogger

def test_structured_logger():
    logger = StructuredLogger(app_name="simple_logger", app_version="v0.0.1")
    logger.info({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})