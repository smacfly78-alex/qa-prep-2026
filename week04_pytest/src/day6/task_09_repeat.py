from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

if __name__ == '__main__':
    @repeat(3)
    def say_hello(name: str) -> str:
        print(f"Hello, {name}")
        return f"Greeted {name}"


    result = say_hello("Igor")
    # Hello, Igor
    # Hello, Igor
    # Hello, Igor

    print(result)


    # Greeted Igor (последний возврат)

    @repeat(5)
    def add(a: int, b: int) -> int:
        return a + b


    print(add(2, 3))
    # 5 (вызовется 5 раз, последний результат - 5)