from typing import Callable, Iterator

def get_user_ids(users: list[dict]) -> list[int]:
    """Extracts 'id' from each user dict."""
    return [user["id"] for user in users]

def divide(a: float, b: float) -> float | None:
    """Divides a by b. Returns None if b is 0."""
    if b == 0:
        return None
    return a / b

def apply_discount(price: float, percent: float) -> float:
    """Applies percent discount to price. Returns new price."""
    return price * (1 - percent / 100)

def make_greeter(greeting: str) -> Callable[[str], str]:
    """Returns a function that greets by name."""
    def greeter(name):
        return f"{greeting}, {name}"
    return greeter

def running_max(numbers: list[float]) -> Iterator[float]:
    """Yields running max of numbers."""
    current_max = float("-inf")
    for n in numbers:
        current_max = max(current_max, n)
        yield current_max