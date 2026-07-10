import random
from typing import Iterator


def random_numbers(minimum: int = 1, maximum: int = 100) -> Iterator[int]:
    while True:
        yield random.randint(minimum, maximum)


if __name__ == '__main__':
    from itertools import islice

    gen = random_numbers()

    # Первые 5 значений
    first_five = list(islice(gen, 5))
    print(first_five)  # [45, 78, 12, 90, 3]  (случайные)

    # Ещё 3 (генератор продолжает — не пересоздаётся)
    next_three = list(islice(gen, 3))
    print(next_three)  # [22, 66, 99]  (тоже случайные)

    # Диапазон 1-10
    gen2 = random_numbers(minimum=1, maximum=10)
    print(list(islice(gen2, 4)))  # [5, 3, 8, 2]