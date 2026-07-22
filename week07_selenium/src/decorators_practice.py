from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(n):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return decorator