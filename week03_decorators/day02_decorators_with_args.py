from functools import wraps
from unittest import result


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for number in range(1, n+1):
                print(f'Run {number}/{n}')
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(n=3)
def greet(name: str) -> None:
    print(f"Hello, {name}!")


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

@validate_range(0, 100)
def calculate_score(correct: int, total: int) -> int:
    return int((correct / total) * 100)


@validate_range(min_val=18, max_val=120)
def get_age() -> int:
    return 25


@validate_range(0, 100)
def buggy_score() -> int:
    return 150     # выходит за диапазон!

if __name__ == "__main__":
    print(calculate_score(8, 10))  # Должен быть OK, 80
    print(get_age())  # OK, 25
    print(buggy_score())  # WARN, 150

    greet("Igor")