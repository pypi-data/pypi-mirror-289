# ai_logstash

A versatile logging package that supports both synchronous and asynchronous logging in Python, with Logstash integration for centralized log management and monitoring.

## Features

- Supports both synchronous and asynchronous logging
- Integrates seamlessly with Logstash
- Masks sensitive information automatically
- Provides decorators for automatic exception logging
- Includes environment variables and local variables in logs
- Compatible with various Python applications, including FastAPI and Aiogram

## Installation

### Using pipenv (recommended)

```
[packages]
pipenv install ai_logstash
```

### Using pip

```bash
pip install ai_logstash
```

## Usage

### Synchronous Logging

```python
from ai_logstash import SyncAiLogger, sync_log_exception

logger = SyncAiLogger(
    'my-service',
    project_name="work_wallet",
    masked_variables_names=["PRIVATE", "password", "api_key"],
    logstash_host="logstash.example.com",
    logstash_port=5000,
    container_tag="1.0",
    environment="production"
)

@sync_log_exception(logger)
def my_function():
    logger.info("Starting my_function")
    # Your code here
```

### Asynchronous Logging (e.g., for FastAPI or Aiogram)

```python
from ai_logstash import AsyncAiLogger, create_async_error_handler

logger = AsyncAiLogger(
    'my-async-service',
    project_name="work_wallet",
    masked_variables_names=["PRIVATE", "password", "api_key"],
    logstash_host="logstash.example.com",
    logstash_port=5000,
    container_tag="1.0",
    environment="production"
)

errors_handler = create_async_error_handler(logger)

@errors_handler
async def my_async_function():
    await logger.info("Starting my_async_function")
    # Your async code here
```

## Configuration

- `service_name`: Name of your service
- `project_name`: Name of your project (work_wallet, payout_bot, etc.)
- `masked_variables_names`: List of sensitive variable names to be masked
- `logstash_host`: Hostname of your Logstash server
- `logstash_port`: Port of your Logstash server
- `container_tag`: Tag for container version
- `environment`: Deployment environment (e.g., "production", "development")
- `log_level`: Logging level (default: "INFO")

## Benefits

- Centralized logging with Logstash integration
- Automatic masking of sensitive information
- Easy integration with various Python frameworks
- Supports both synchronous and asynchronous applications
- Includes detailed error information and environment variables
