
class Product:
    def __init__(self, name: str, sku: str) -> None:
        self.name = name
        self.sku = sku

    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return False
        return self.sku == other.sku

    def __hash__(self):
        return hash(self.sku)

    def __repr__(self):
        return f"Product(name={self.name!r}, sku={self.sku!r})"