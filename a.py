from src.structlog_telemetry.structlog_telemetry import StructLogTelemetry




logger = StructLogTelemetry("app", "0.1.1", print_banner = False)

logger.info("Hello")
logger.error("my error")
logger.warning("critical")