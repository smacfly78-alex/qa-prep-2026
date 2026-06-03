
class Vehicle:
    def __init__(self, brand: str, year: int) -> None:
        self.brand = brand
        self.year = year

    def info(self) -> str:
        return f'{self.brand}, {self.year}'

    def start(self) -> str:
        return f'{self.brand} запускается'

class Car(Vehicle):
    def __init__(self, brand: str, year: int, num_doors: int) -> None:
        super().__init__(brand, year)
        self.num_doors = num_doors

    def info(self) -> str:
        return f'{super().info()}, {self.num_doors} дверей'

    def honk(self) -> str:
        return 'Beep!'


class Motorcycle(Vehicle):
    def __init__(self, brand: str, year: int, has_sidecar: bool) -> None:
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar


    def info(self) -> str:
        if self.has_sidecar:
            return f'{super().info()}, с коляской'
        else:
            return f'{super().info()}, без коляски'

    def wheelie(self) -> str:
        return f'{self.brand} едет на одном колесе!'

# ------------------------------------------------------------

class User:
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.set_password(password)

    def set_password(self, new_password: str) -> None:
        if len(new_password) >= 8:
            self._password = new_password
        else:
            raise ValueError('Not enough characters!')

    def check_password(self, password: str) -> bool:
        return password == self._password

    def info(self) -> str:
        return f'User: {self.name}'


class AdminUser(User):
    def __init__(self, name: str, password: str, permissions: list[str]) -> None:
        super().__init__(name, password)
        self.permissions = permissions

    def info(self) -> str:
        return f'Admin: {self.name}, права: {self.permissions}'

    def has_permission(self, perm: str) -> bool:
        return perm in self.permissions



if __name__ == '__main__':
    u = User("Igor", "secret123")
    print(u.info())  # "User: Igor"
    print(u.check_password("secret123"))  # True

    a = AdminUser("Anna", "topsecret", ["delete", "ban", "edit"])
    print(a.info())  # "Admin: Anna, права: ['delete', 'ban', 'edit']"
    print(a.check_password("topsecret"))  # True — метод от родителя работает!
    print(a.has_permission("delete"))  # True
    print(a.has_permission("create"))  # False


    c = Car("Toyota", 2020, 4)
    print(c.info())  # "Toyota, 2020, 4 дверей"
    print(c.start())  # "Toyota запускается" — от родителя!
    print(c.honk())  # "Beep!"

    m = Motorcycle("Harley", 2018, True)
    print(m.info())  # "Harley, 2018, с коляской"
    print(m.start())  # "Harley запускается"
    print(m.wheelie())  # "Harley едет на одном колесе!"

    # Проверка isinstance
    print(isinstance(c, Car))  # True
    print(isinstance(c, Vehicle))  # True — через наследование!
    print(isinstance(c, Motorcycle))  # False