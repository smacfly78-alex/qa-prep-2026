
class RangeSquares:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.start = 1
        self.current = 1

    def __iter__(self) -> 'RangeSquares':
        return self

    def __next__(self) -> int:
        if self.start <= self.current <= self.limit:
            result = self.current
            self.current += 1
            return result ** 2
        else:
            raise StopIteration

if __name__ == '__main__':
    squares = RangeSquares(4)
    for n in squares:
        print(n, end=" ")
    # 1 4 9 16

    print()
    print(list(RangeSquares(5)))
    # [1, 4, 9, 16, 25]

    print(list(RangeSquares(1)))
    # [1]

    print(list(RangeSquares(0)))
    # []  (пусто — от 1 до 0 нет чисел)

    # Ручной вызов
    it = iter(RangeSquares(3))
    print(next(it))  # 1
    print(next(it))  # 4
    print(next(it))  # 9
    # next(it) — StopIteration!