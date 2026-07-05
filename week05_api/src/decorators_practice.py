from collections.abc import Callable
from functools import wraps


def log_with(prefix: str) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{prefix}: calling {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

if __name__ == "__main__":
    @log_with("INFO")
    def greet(name: str) -> str:
        return f"Hello, {name}"


    @log_with("DEBUG")
    def add(a: int, b: int) -> int:
        return a + b


    print(greet("Igor"))
    # INFO: calling greet
    # Hello, Igor

    print(add(5, 10))


    # DEBUG: calling add
    # 15

    # Кроме одного декоратора, можно применить два
    @log_with("A")
    @log_with("B")
    def multiply(x: int, y: int) -> int:
        return x * y


    print(multiply(3, 4))
    # A: calling wrapper       ← ой, wrapper, не multiply!
    # B: calling multiply
    # 12