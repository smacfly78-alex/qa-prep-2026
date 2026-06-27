from collections.abc import Callable


def make_calculator() -> tuple[Callable, Callable, Callable]:
    # value инициализируется как 0
    value = 0

    def add(n: int) -> int:
        nonlocal value
        # увеличивает value на n, возвращает новое value
        value += n
        return value

    def subtract(n: int) -> int:
        # уменьшает value на n, возвращает новое value
        nonlocal value
        value -= n
        return value

    def get_value() -> int:
        # возвращает текущее value
        return value

    return add, subtract, get_value

if __name__ == '__main__':
    add, sub, get = make_calculator()

    print(add(10))  # 10
    print(add(5))  # 15
    print(sub(3))  # 12
    print(get())  # 12

    # Второй вызов make_calculator — независимая копия
    add2, sub2, get2 = make_calculator()
    print(add2(100))  # 100 (свой value, начинается с 0)
    print(get())  # 12 (первый калькулятор не затронут)