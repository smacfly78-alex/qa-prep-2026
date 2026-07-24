from typing import Iterator


def fibonacci(n: int) -> Iterator[int]:
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    print(list(fibonacci(0)))  # []
    print(list(fibonacci(1)))  # [0]
    print(list(fibonacci(2)))  # [0, 1]
    print(list(fibonacci(7)))  # [0, 1, 1, 2, 3, 5, 8]