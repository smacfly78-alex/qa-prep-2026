class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        self.value += 1

    def reset(self) -> None:
        self.value = 0