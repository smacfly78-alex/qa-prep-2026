from functools import wraps


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end = time.perf_counter()
            elapsed = end - start
            print(f'[timing] {func.__name__} took {elapsed:.2f} seconds')
    return wrapper

if __name__ == '__main__':
    import time


    @timing
    def slow_function(n: int) -> int:
        """Долгая функция."""
        time.sleep(n)
        return n * 10


    result = slow_function(1)
    # [timing] slow_function took 1.00 seconds
    print(result)  # 10


    @timing
    def quick_add(a: int, b: int) -> int:
        return a + b


    print(quick_add(2, 3))


    # [timing] quick_add took 0.00 seconds
    # 5

    # Работа с исключениями
    @timing
    def failing_function():
        time.sleep(0.5)
        raise ValueError("Boom")


    try:
        failing_function()
    except ValueError:
        pass
    # [timing] failing_function took 0.50 seconds
    # (даже при исключении — время печатается!)


