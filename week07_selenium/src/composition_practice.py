class Engine:
    def start(self) -> None:
        print('Engine started')


class Car:
    def __init__(self, name: str) -> None:
        self.name = name
        self.engine = Engine()  # композиция

    def drive(self) -> None:
        self.engine.start()
        print(f'Car {self.name} is driving')


class Garage:
    def __init__(self) -> None:
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def get_cars(self) -> None:
        for car in self.cars:
            print(car.name)