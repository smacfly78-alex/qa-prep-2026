
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError('Sub zero!')
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32



class User:
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.set_password(password)

    def set_password(self, new_password: str) -> None:
        if len(new_password) < 8:
            raise ValueError('Not enough characters!')
        self._password = new_password

    def check_password(self, password: str) -> bool:
        return password == self._password



if __name__ == '__main__':

    u = User("Igor", "secret123")
    print(u.name)  # "Igor"

    print(u.check_password("wrong"))  # False
    print(u.check_password("secret123"))  # True

    u.set_password("newsecret")
    print(u.check_password("secret123"))  # False (старый больше не работает)
    print(u.check_password("newsecret"))  # True

    try:
        u.set_password("123")
    except ValueError as e:     # ValueError: пароль короткий
        print(f"Ошибка: {e}")


    t = Temperature(20)
    print(t.celsius)  # 20
    print(t.fahrenheit)  # 68.0

    t.celsius = 100
    print(t.celsius)  # 100
    print(t.fahrenheit)  # 212.0

    try:
        t.celsius = -300
    except ValueError as e:     # ValueError: ниже абсолютного нуля
        print(f"Ошибка: {e}")
