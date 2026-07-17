class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, percent: int) -> None:
        new_price = self.price * (1 - percent / 100)
        if new_price < 0:
            self.price = 0
        else:
            self.price = new_price

    def is_available(self) -> bool:
        return self.stock > 0

    def __str__(self) -> str:
        return f'Product: {self.name} (${self.price}, stock={self.stock})'


class DigitalProduct(Product):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, stock = 0)

    def is_available(self) -> bool:
        return True

if __name__ == '__main__':
    p = Product("Laptop", 1000.0, 5)
    print(p)  # Product: Laptop ($1000.0, stock=5)
    print(p.is_available())  # True

    p.apply_discount(20)  # -20% от 1000 = 800
    print(p)  # Product: Laptop ($800.0, stock=5)

    # Слишком большая скидка
    p.apply_discount(200)  # -200% → должно стать 0
    print(p)  # Product: Laptop ($0, stock=5)

    d = DigitalProduct("ebook.pdf", 15.0)
    print(d)  # Product: ebook.pdf ($15.0, stock=?)
    print(d.is_available())  # True (всегда)