# StructLog-Telemetry
Structlog-Telemetry is a very simple custom Python structured logger library.

[![unittests](https://github.com/cyber-francis/structlog_telemetry/actions/workflows/pytest.yaml/badge.svg)](https://github.com/cyber-francis/structlog_telemetry/actions/workflows/pytest.yaml)[![release](https://github.com/cyber-francis/structlog_telemetry/actions/workflows/release.yaml/badge.svg)](https://github.com/cyber-francis/structlog_telemetry/actions/workflows/release.yaml)

## Installation
```bash
python3 -m pip install structlog-telemetry
```

## Usage

```python
from structlog_telemetry.structlog_telemetry import StructLogTelemetry

APP_NAME = "APP_X"
APP_VERSION = "v0.0.1"
logger = StructLogTelemetry(APP_NAME, APP_VERSION)


logger.info("hello world")
logger.warning("Hello world")
logger.error("hello world")
```
<img src="https://raw.githubusercontent.com/cyber-francis/structlog_telemetry/main/docs/log.png">

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
