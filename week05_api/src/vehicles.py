from functools import wraps


class Engine:
    def start(self) -> str:
        return 'Engine started'

class Car:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.engine = Engine()

    def drive(self) -> str:
        result = self.engine.start()
        return f'{self.brand} is driving. {result}'

def repeat_and_collect(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            items = []
            for number in range(n):
                items.append(func(*args, **kwargs))
            return items
        return wrapper
    return decorator

@repeat_and_collect(n=3)
def get_random() -> int:
    import random
    return random.randint(1, 100)

if __name__ == '__main__':
    results = get_random()
    print(results)
    # [45, 78, 12]  ← три разных вызова, разные результаты
    print(len(results))


    car = Car("Ferrari")
    print(car.drive())
    # Ferrari is driving. Engine started

    toyota = Car("Toyota")
    print(toyota.drive())
    # Toyota is driving. Engine started

    # У каждой машины СВОЙ engine
    print(car.engine is toyota.engine)  # False

