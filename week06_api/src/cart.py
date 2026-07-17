
class Cart:
    def __init__(self) -> None:
        self.items = {}

    def add(self, product: str, quantity: int = 1) -> None:
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove(self, product: str) -> None:
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(product)

    def total_items(self) -> int:
        return sum(self.items.values())

    def unique_products(self) -> int:
        return len(self.items.keys())

    def __str__(self) -> str:
        return f'Cart: {self.unique_products()} products, {self.total_items()} items'


if __name__ == '__main__':
    cart = Cart()
    print(cart)  # Cart: 0 products, 0 items

    cart.add("apple", 3)
    cart.add("banana", 2)
    cart.add("apple", 1)  # добавили ещё apple → total apple = 4

    print(cart)  # Cart: 2 products, 6 items
    print(cart.total_items())  # 6
    print(cart.unique_products())  # 2

    cart.remove("banana")
    print(cart)  # Cart: 1 products, 4 items

    # Удаление отсутствующего
    try:
        cart.remove("orange")
    except KeyError as e:
        print(f"Not found: {e}")