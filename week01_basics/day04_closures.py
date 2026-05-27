from typing import Callable

def make_power(exponent: int) -> Callable[[int], int]:
    def raise_to_power(base: int) -> int:
         return base ** exponent
    return raise_to_power

def make_validator(min_length: int) -> Callable[[str], bool]:
    def func_val(phrase: str) -> bool:
        return len(phrase) >= min_length
    return func_val

def make_counter() -> tuple[Callable[[], int], Callable[[], None]]:
    counter = 0
    def increment() -> int:
        nonlocal counter
        counter = counter + 1
        return counter

    def reset() -> None:
        nonlocal counter
        counter = 0

    return increment, reset


if __name__ == '__main__':
    # Power
    square = make_power(2)
    cube = make_power(3)
    print(square(5))  # 25
    print(cube(3))  # 27

    # Validator (после исправления >= )
    password_validator = make_validator(8)
    print(password_validator("12345"))  # False
    print(password_validator("supersecret"))  # True
    print(password_validator("12345678"))  # True — граничный случай!

    # Counter
    increment, reset = make_counter()
    print(increment())  # 1
    print(increment())  # 2
    print(increment())  # 3
    reset()
    print(increment())  # 1