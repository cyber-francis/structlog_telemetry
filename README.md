<div align="center">
<p align="center">
<img src="structlog_telemetery.drawio.png">
</p>

A very simple custom structured logger
</div>

## How To Use
### Step 1 - Install
```python3 -m pip install -i https://test.pypi.org/simple/ structlog-telemetry==0.0.7```

### Step 2 - Import and Use
```
>>> from structlog_telemetry import structured_logger
>>> logger = structured_logger.StructuredLogger(app_name="simple_logger", app_version="v0.0.1")
>>> logger.info({"EVENT": {"TYPE": "ACCESS", "NAME": "USER_NOT_FOUND"}})
2023-12-31 16:22:30 [info     ] {'APP_NAME': 'simple_logger', 'APP_VERSION': 'v0.0.1', 'EVENT': {'EVENT': {'TYPE': 'ACCESS', 'NAME': 'USER_NOT_FOUND'}}}
```
