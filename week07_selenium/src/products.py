
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f"{self.name}: ${self.price:.2f}"


class DigitalProduct(Product):
    def __init__(self, name: str, price: float, file_size_mb: int) -> None:
        super().__init__(name, price)
        self.file_size_mb = file_size_mb

    def get_info(self) -> str:
        return f'{super().get_info()} ({self.file_size_mb} MB)'