from typing import Iterator


def even_squares(n: int) -> Iterator[int]:
    for number in range(n):
        if number % 2 == 0:
            yield number ** 2

if __name__ == "__main__":
    gen = even_squares(6)
    print(list(gen))
    # [0, 4, 16]   ← только 0, 2, 4 — их квадраты

    for x in even_squares(10):
        print(x)
    # 0
    # 4
    # 16
    # 36
    # 64

    # Пустой случай
    print(list(even_squares(0)))
    # []

    # Только один элемент (0)
    print(list(even_squares(1)))
    # [0]