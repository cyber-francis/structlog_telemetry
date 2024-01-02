from src.structlog_telemetry.structlog_telemetry import StructLogTelemetry
import pytest


def call_logger(logger):
    logger.debug({"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"})
    logger.info({"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"})
    logger.warning({"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"})
    logger.error({"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"})
    logger.exception({"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"})
    logger.critical({"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"})


@pytest.mark.run(order=1)
def test_structured_logger_with_json_renderer():
    logger = StructLogTelemetry(
        app_name="simple_logger", app_version="v0.0.1", json_renderer=True
    )
    call_logger(logger)
    del logger


@pytest.mark.run(order=2)
def test_structured_logger_without_json_renderer():
    logger = StructLogTelemetry(
        app_name="simple_logger", app_version="v0.0.1", json_renderer=False
    )
    call_logger(logger)
