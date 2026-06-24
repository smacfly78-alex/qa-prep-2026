from collections.abc import Callable


def make_adder(value: int) -> Callable[[int], int]:
    def add(n: int) -> int:
        return n + value
    return add

if __name__ == '__main__':
    add5 = make_adder(5)
    add10 = make_adder(10)

    print(add5(3))  # 8
    print(add5(100))  # 105
    print(add10(3))  # 13
    print(add10(100))  # 110

    print(add5(3) + add10(3))  # 8 + 13 = 21