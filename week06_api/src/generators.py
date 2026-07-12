import random
from typing import Iterator, Any, Generator


def random_numbers(minimum: int = 1, maximum: int = 100) -> Iterator[int]:
    while True:
        yield random.randint(minimum, maximum)


class Employee:
    role: str = "employee"

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        # ← ИСПРАВЬТЕ ЗДЕСЬ
        return f"I am {self.name}, a {self.role}"


class Manager(Employee):
    role = "manager"


class Intern(Employee):
    role = "intern"


def fibonacci(n: int) -> Iterator[int]:
    a = 0
    b = 1
    for num in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    m = Manager("Igor")
    i = Intern("Anna")
    e = Employee("Bob")

    print(m.introduce())  # I am Igor, a manager
    print(i.introduce())  # I am Anna, a intern
    print(e.introduce())  # I am Bob, a employee


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