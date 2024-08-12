import asyncio
import json
import logging
import os
import sys
import traceback
from typing import Optional

from logstash_async.formatter import LogstashFormatter
from logstash_async.handler import AsynchronousLogstashHandler
from ai_logstash.version import __version__


def build_exception_extra(masked_variables_names):
    exc_type, exc_value, exc_traceback = sys.exc_info()

    env_vars = dict(os.environ)
    for key in masked_variables_names:
        env_vars = {
            k: v if k.lower().find(key) == -1 else "REDACTED"
            for k, v in env_vars.items()
        }
    formatted_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)

    tb = exc_traceback
    while tb.tb_next:
        tb = tb.tb_next
    frame = tb.tb_frame

    safe_locals = {}
    for key, value in frame.f_locals.items():
        if any(
            sensitive_name in key.lower() for sensitive_name in masked_variables_names
        ):
            safe_locals[key] = "REDACTED"
        else:
            try:
                json.dumps({key: value})
                safe_locals[key] = value
            except TypeError:
                safe_locals[key] = repr(value)

    return {
        "exception_type": exc_type.__name__,
        "exception_message": str(exc_value),
        "traceback": json.dumps(formatted_traceback),
        "local_variables": json.dumps(safe_locals),
        "environment_variables": json.dumps(env_vars),
        "ai_logstash_version": __version__,
    }


class BaseAiLogger:
    def __init__(
        self,
        service_name: str,
        project_name: str,
        masked_variables_names: Optional[list[str]] = None,
        logstash_host=None,
        logstash_port=None,
        container_tag: str = "unknown",
        environment: str = "unknown",
        log_level: str = "INFO",
    ):
        default_masked_variables = ["password", "secret", "api_key", "token", "private"]
        if masked_variables_names is None:
            masked_variables_names = []

        all_masked_variables = default_masked_variables + masked_variables_names
        self.logger = logging.getLogger(service_name)
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f"Invalid log level: {log_level}")

        self.logger.setLevel(numeric_level)
        self.logstash_port = logstash_port
        self.masked_variables_names = list(
            set(var.lower() for var in all_masked_variables)
        )
        console_handler = logging.StreamHandler()
        console_handler.setLevel(numeric_level)
        self.logstash_host = logstash_host
        self.logger.addHandler(console_handler)
        self.default_extra = {
            "service_name": service_name,
            "container_tag": container_tag,
            "environment": environment,
            "project": project_name,
        }

        if self.logstash_host:
            logstash_handler = AsynchronousLogstashHandler(
                self.logstash_host, self.logstash_port, database_path=None
            )
            formatter = LogstashFormatter()
            logstash_handler.setFormatter(formatter)
            self.logger.addHandler(logstash_handler)


class SyncAiLogger(BaseAiLogger):
    def _log(self, level, message, extra=None):
        log_extra = self.default_extra.copy()
        if extra is not None:
            log_extra.update(extra)
        self.logger.log(level, message, extra=log_extra)

    def info(self, message, extra=None):
        self._log(logging.INFO, message, extra)

    def warning(self, message, extra=None):
        self._log(logging.WARNING, message, extra)

    def error(self, message, extra=None):
        self._log(logging.ERROR, message, extra)

    def exception(self, message, extra=None):
        if extra is None:
            extra = {}
        extra.update(build_exception_extra(self.masked_variables_names))
        self._log(logging.ERROR, message, extra)


class AsyncAiLogger(BaseAiLogger):
    async def _log(self, level, message, extra=None):
        log_extra = self.default_extra.copy()
        if extra is not None:
            log_extra.update(extra)
        await asyncio.to_thread(self.logger.log, level, message, extra=log_extra)

    async def info(self, message, extra=None):
        await self._log(logging.INFO, message, extra)

    async def warning(self, message, extra=None):
        await self._log(logging.WARNING, message, extra)

    async def error(self, message, extra=None):
        await self._log(logging.ERROR, message, extra)

    async def exception(self, message, extra=None):
        if extra is None:
            extra = {}
        extra.update(build_exception_extra(self.masked_variables_names))
        await self._log(logging.ERROR, message, extra)
