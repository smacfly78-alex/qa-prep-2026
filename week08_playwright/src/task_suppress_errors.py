
class SuppressErrors:
    def __init__(self, *args):
        self.errors = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            return None
        if isinstance(exc_val, self.errors):
            return True
        return None

if __name__ == '__main__':
    # Пример 1 — подавляет ValueError
    with SuppressErrors(ValueError):
        print("Start")
        raise ValueError("This won't crash")
        print("Skipped")  # не выполнится

    print("After block")  # выполнится!

    # Пример 2 — не подавляет другие исключения
    try:
        with SuppressErrors(ValueError):
            raise TypeError("Not suppressed!")
    except TypeError as e:
        print(f"Caught outside: {e}")
    # Caught outside: Not suppressed!

    # Пример 3 — множественные типы
    with SuppressErrors(ValueError, KeyError):
        d = {}
        print(d["missing"])  # KeyError, подавлен

    print("Still running")

    # Пример 4 — работает и без исключений
    with SuppressErrors(ValueError):
        print("Normal execution")

    print("After normal")