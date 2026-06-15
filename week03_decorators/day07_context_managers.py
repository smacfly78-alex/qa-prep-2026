import time
from contextlib import contextmanager



class Timer:
    def __init__(self, label: str = 'Block') -> None:
        self.label = label

    def __enter__(self) -> "Timer":
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        result = time.time() - self.start
        print(f'{self.label} took {result} seconds')

@contextmanager
def timer_func(label: str = 'Block'):
    start = time.time()
    try:
        yield
    finally:
        result = time.time() - start
        print(f'{label} took {result} seconds')

if __name__ == '__main__':
    with timer_func() as t:
        time.sleep(0.5)
        sum(x ** 2 for x in range(100_000))

    # Вывод: Block took 0.5xxx seconds

    with timer_func("Heavy computation"):
        time.sleep(0.3)
        sum(x ** 3 for x in range(50_000))

    # Вывод: Heavy computation took 0.3xxx seconds

    # Бонусная проверка — что try/finally работает при исключении
    try:
        with timer_func("Failing block"):
            time.sleep(0.2)
            raise ValueError("test error")
    except ValueError:
        print("Caught the error, but timer printed before that!")

    # with Timer() as t:
    #     time.sleep(0.5)
    #     sum(x ** 2 for x in range(100_000))
    #
    # # Вывод: Block took 0.5xxx seconds
    #
    # with Timer("Heavy computation"):
    #     time.sleep(0.3)
    #     sum(x ** 3 for x in range(50_000))
    #
    # # Вывод: Heavy computation took 0.3xxx seconds