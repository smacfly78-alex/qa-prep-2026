from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self) -> str:
        return f'Фигура с площадью {self.area()} и периметром {self.perimeter()}'


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def total_area(shapes: list[Shape]) -> float:
    result = 0
    for shape in shapes:
        result += shape.area()
    return result



class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass


class EmailNotifier(Notifier):
    def __init__(self, email_address: str) -> None:
        self.email_address = email_address

    def send(self, message: str) -> str:
        return f'Email на {self.email_address}: {message}'


class SmsNotifier(Notifier):
    def __init__(self, phone: str) -> None:
        self.phone = phone

    def send(self, message: str) -> str:
        return f"SMS на {self.phone}: {message}"


class SlackNotifier(Notifier):
    def __init__(self, channel: str) -> None:
        self.channel = channel

    def send(self, message: str) -> str:
        return f"Slack в {self.channel}: {message}"

def broadcast(notifiers: list[Notifier], message: str) -> list[str]:
    result = []
    for notifier in notifiers:
        result.append(notifier.send(message))
    return result


if __name__ == '__main__':
    notifiers = [
        EmailNotifier("admin@example.com"),
        SmsNotifier("+79991234567"),
        SlackNotifier("#alerts"),
    ]

    results = broadcast(notifiers, "Сервер недоступен!")
    for r in results:
        print(r)

    # Email на admin@example.com: Сервер недоступен!
    # SMS на +79991234567: Сервер недоступен!
    # Slack в #alerts: Сервер недоступен!


    c = Circle(5)
    r = Rectangle(4, 6)

    print(c.area())  # 78.5
    print(c.perimeter())  # 31.4
    print(c.describe())  # "Фигура с площадью 78.5 и периметром 31.4"

    print(r.area())  # 24
    print(r.describe())  # "Фигура с площадью 24 и периметром 20"

    print(total_area([c, r]))  # 102.5

    # Проверка абстрактности
    try:
        s = Shape()
    except TypeError as e:
        print(f"Ошибка: {e}")