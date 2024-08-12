import sys
import traceback
from functools import wraps
from typing import Any, Callable

from .logger import AsyncAiLogger, SyncAiLogger


def create_async_error_handler(logger: AsyncAiLogger):
    def error_handler(func: Callable):
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                tb = traceback.extract_tb(exc_traceback)
                filename, line, func_name, text = tb[-1]

                error_message = (
                    f"Unhandled exception {exc_type.__name__} raised in {func_name} function.\n"
                    f"File '{filename}', line {line}, in {func_name}\n"
                    f"{text}\n"
                    f"Error: {str(e)}"
                )

                extra = {
                    "exception_type": exc_type.__name__,
                    "exception_message": str(e),
                    "traceback": traceback.format_exc(),
                    "handler_function": func.__name__,
                    "file": filename,
                    "line": line,
                }
                await logger.exception(error_message, extra=extra)
                raise

        return wrapper

    return error_handler


def sync_log_exception(logger: SyncAiLogger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                _, _, exc_traceback = sys.exc_info()
                tb = exc_traceback
                while tb.tb_next:
                    tb = tb.tb_next
                frame = tb.tb_frame
                func_name = frame.f_code.co_name
                logger.exception(
                    f"Unhandled exception {e.__class__.__name__} raised in {func_name} function."
                )
                raise

        return wrapper

    return decorator
