import time


class Timer:
    def __init__(self, name: str = "Task") -> None:
        self.name = name
        self._elapsed: float = 0.0

    def __enter__(self) -> "Timer":
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        end = time.perf_counter()
        self._elapsed = end - self.start
        print(f'[{self.name}] took {self._elapsed:.3f} seconds')

    @property
    def elapsed(self) -> float:
        return self._elapsed

if __name__ == "__main__":

    with Timer("sleep test") as timer:
        time.sleep(0.5)

    # [sleep test] took 0.500 seconds

    print(timer.elapsed)
    # 0.5023456 (примерное значение)

    # С исключением — Timer печатает, но не подавляет
    try:
        with Timer("failing task") as timer:
            raise ValueError("oops")
    except ValueError:
        print(f"Caught. Time was: {timer.elapsed}")

    # [failing task] took 0.000 seconds
    # Caught. Time was: 0.000012