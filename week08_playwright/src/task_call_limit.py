from functools import wraps


def call_limit(n):
    def decorator(func):
        count = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            while count < n:
                result = func(*args, **kwargs)
                count += 1
                return result
            raise RuntimeError(f"Call limit {n} exceeded")
        return wrapper
    return decorator

if __name__ == '__main__':
    @call_limit(3)
    def greet(name: str) -> str:
        return f"Hello, {name}!"


    print(greet("Igor"))  # Hello, Igor!
    print(greet("Anna"))  # Hello, Anna!
    print(greet("Sam"))  # Hello, Sam!

    try:
        print(greet("Kate"))
    except RuntimeError as e:
        print(f"Error: {e}")


    # Error: Call limit (3) exceeded

    # Второй декорированный — свой счётчик
    @call_limit(2)
    def double(x: int) -> int:
        return x * 2


    print(double(5))  # 10
    print(double(10))  # 20

    try:
        print(double(15))
    except RuntimeError as e:
        print(f"Error: {e}")
    # Error: Call limit (2) exceeded