
class Reverse:
    def __init__(self, items: list) -> None:
        self.items = items
        self.start = len(self.items)
        self.limit = 0

    def __iter__(self) -> 'Reverse':
        return self

    def __next__(self):
        if self.start > self.limit:
            result = self.start
            self.start -= 1
            return self.items[result - 1]
        else:
            raise StopIteration


if __name__ == '__main__':
    r = Reverse([1, 2, 3, 4, 5])
    for item in r:
        print(item, end=" ")
    # 5 4 3 2 1

    print()
    print(list(Reverse(["a", "b", "c"])))
    # ['c', 'b', 'a']

    print(list(Reverse([])))
    # []

    print(list(Reverse([42])))
    # [42]

    # Ручной вызов
    it = iter(Reverse([10, 20, 30]))
    print(next(it))  # 30
    print(next(it))  # 20
    print(next(it))  # 10
    # next(it) → StopIteration