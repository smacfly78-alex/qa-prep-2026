from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0] <= 0:
            raise ValueError("Argument must be positive")
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    @validate_positive
    def square_root(x: float) -> float:
        return x ** 0.5


    print(square_root(16))  # 4.0
    print(square_root(25))  # 5.0
    print(square_root(-4))  # ValueError: Argument must be positive
    print(square_root(0))  # ValueError: Argument must be positive