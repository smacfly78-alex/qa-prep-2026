import random
from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f'[TIMER] {func.__name__} took {duration:.4f} seconds')
        return result
    return wrapper

@timer
def slow_function(n: int) -> int:
    """Медленная функция для теста — считает сумму."""
    total = 0
    for i in range(n):
        total += i
    return total

@timer
def fast_greeting(name: str) -> str:
    return f"Hello, {name}!"

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
                last_error = None
                for number in range(1, times+1):
                    print(f'[RETRY] Attempt {number}/{times} for {func.__name__}')
                    try:
                        result = func(*args, **kwargs)
                        return result
                    except Exception as e:
                        last_error = e
                        print(f'[RETRY] Failed: {e}')
                raise last_error

        return wrapper
    return decorator

@retry(times=3)
def unreliable_request() -> str:
    """Симулирует нестабильный запрос — падает в 70% случаев."""
    if random.random() < 0.7:
        raise ConnectionError("Network timeout")
    return "Success!"


if __name__ == '__main__':
    for _ in range(5):
        print("---")
        try:
            result = unreliable_request()
            print(f"Got: {result}")
        except ConnectionError as e:
            print(f"Final failure: {e}")
    # # Вызовы
    # result1 = slow_function(1_000_000)
    # print(f"Result: {result1}")
    #
    # result2 = fast_greeting("Igor")
    # print(f"Result: {result2}")

