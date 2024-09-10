import os
from functools import wraps
from typing import Any, Callable


def temporary_chdir(path: str) -> None:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            old_dir = os.getcwd()
            os.chdir(path)
            try:
                result = func(*args, **kwargs)
            finally:
                os.chdir(old_dir)
            return result

        return wrapper

    return decorator
