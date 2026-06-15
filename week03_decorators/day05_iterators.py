
class ProgressIterator:
    def __init__(self, items: list) -> None:
        self.items = items
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.items):
            raise StopIteration
        value = self.items[self.position]
        self.position += 1
        return value

    @property
    def progress(self) -> float:
        if len(self.items) == 0:
            return 0.0
        return self.position / len(self.items) * 100

if __name__ == '__main__':
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    iterator = ProgressIterator(items)

    for item in iterator:
        print(f"{item} — progress: {iterator.progress:.1f}%")
