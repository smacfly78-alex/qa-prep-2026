
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

if __name__ == '__main__':
    t = Temperature(20)
    print(t.celsius)  # 20

    t.celsius = 25
    print(t.celsius)  # 25

    t.celsius = -300  # ValueError: Temperature below absolute zero