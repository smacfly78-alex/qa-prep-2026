import time
from functools import wraps
from typing import Iterator


def greet(name: str, greeting: str = "Hello") -> str:
    return f'{greeting}, {name}!'

def print_all(**kwargs: object) -> None:
    for key, value in kwargs.items():
        print(f'{key}: {value}')

class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start
        self.current = self.start

    def __iter__(self) -> 'Countdown':
        return self

    def __next__(self) -> int:
        if self.current < 1:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

def fibonacci(n: int) -> Iterator[int]:
    a = 0
    b = 1
    for number in range(n):
        yield a
        a, b = b, a + b

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

class Timer:
    def __init__(self) -> None:
        self.start = 0.0
        self.end = 0.0
        self.elapsed = 0.0

    def __enter__(self) -> 'Timer':
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start

def retry(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for i in range(n):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator







if __name__ == '__main__':
    with Timer() as t:
        time.sleep(1)
        # какая-то работа

    print(f"Elapsed: {t.elapsed:.2f} seconds")
    # Elapsed: 1.00 seconds

    # С исключением — timer тоже должен зафиксировать время
    with Timer() as t2:
        time.sleep(0.5)
        raise ValueError("Something failed")

    # Ожидается: исключение всё равно поднимается, но t2.elapsed установлен


    # @log_calls
    # def add(a: int, b: int) -> int:
    #     return a + b
    #
    #
    # @log_calls
    # def greet(name: str, greeting: str = "Hello") -> str:
    #     return f"{greeting}, {name}!"
    #
    #
    # result = add(2, 3)
    # # Calling add with args=(2, 3), kwargs={}
    # # add returned 5
    #
    # print(result)  # 5
    #
    # message = greet("Igor")
    # # Calling greet with args=('Igor',), kwargs={}
    # # greet returned Hello, Igor!
    #
    # message2 = greet("Anna", greeting="Hi")
    # # Calling greet with args=('Anna',), kwargs={'greeting': 'Hi'}
    # # greet returned Hi, Anna!


    # for num in fibonacci(10):
    #     print(num, end=" ")
    # # 0 1 1 2 3 5 8 13 21 34
    #
    # print()
    # print(list(fibonacci(5)))
    # # [0, 1, 1, 2, 3]
    #
    # print(list(fibonacci(1)))
    # # [0]
    #
    # print(list(fibonacci(0)))
    # # []
    #
    # # Ручной вызов
    # gen = fibonacci(3)
    # print(next(gen))  # 0
    # print(next(gen))  # 1
    # print(next(gen))  # 1
    # # next(gen) — StopIteration



    # counter = Countdown(5)
    #
    # for num in counter:
    #     print(num)
    # # 5
    # # 4
    # # 3
    # # 2
    # # 1
    #
    # # Проверка ограничения
    # counter2 = Countdown(3)
    # print(list(counter2))
    # # [3, 2, 1]
    #
    # # Ручной вызов next
    # counter3 = Countdown(2)
    # it = iter(counter3)
    # print(next(it))  # 2
    # print(next(it))  # 1
    # print(next(it))  # StopIteration!


    # print_all(name="Igor", age=30, city="Moscow")
    # # name: Igor
    # # age: 30
    # # city: Moscow
    #
    # print_all()
    # # (ничего не печатает — пустой kwargs)
    #
    # print_all(x=1, y=2)
    # # x: 1
    # # y: 2

    # print(greet("Igor"))  # Hello, Igor!
    # print(greet("Anna", "Hi"))  # Hi, Anna!
    # print(greet(greeting="Hey", name="Sam"))  # Hey, Sam!
