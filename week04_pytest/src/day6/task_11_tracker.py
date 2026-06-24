import time


class Tracker:
    def __init__(self) -> None:
        pass

    def __enter__(self) -> "Tracker":
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.end = time.time()
        self.elapsed = self.end - self.start


if __name__ == '__main__':

    with Tracker() as t:
        time.sleep(1.5)
        print("inside block")

    print(f"Block took {t.elapsed:.2f} seconds")
    # inside block
    # Block took 1.50 seconds

    with Tracker() as t:
        sum(x ** 2 for x in range(1_000_000))

    print(f"Computation took {t.elapsed:.4f} seconds")
    # Computation took 0.0xxx seconds (зависит от машины)