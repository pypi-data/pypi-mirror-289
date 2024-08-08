import functools
from typing import Any, Callable

__all__ = ["return_on_error"]


def return_on_error[T](return_type: T) -> Callable[[Callable], T]:
    """
    These decorators catch :
        - **AttributeError** : In case `selectolax` fails to find the dom node
        - **IndexError** : In case `selectolax` finds empty dom node
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            try:
                return func(*args, **kwargs)
            except (AttributeError, IndexError):
                return return_type

        return wrapper

    return decorator
