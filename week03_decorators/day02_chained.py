import time
from functools import wraps


def validate_range(min_val, max_val):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if min_val <= result <= max_val:
                print(f"[OK] {func.__name__} returned {result} (in range)")
                return result
            print(f"[WARN] {func.__name__} returned {result} (out of range [{min_val}, {max_val}])")
            return result
        return wrapper
    return decorator

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
@validate_range(0, 100)
def compute_score(correct: int, total: int) -> float:
    result = correct / total * 100
    return result


if __name__ == '__main__':
    print(compute_score(8, 10))  # 80 — в диапазоне, OK
    print(compute_score(15, 10))  # 150 — вне диапазона, WARN

