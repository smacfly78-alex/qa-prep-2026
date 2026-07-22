
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)

    points = {p1, p2, p3}
    print(len(points))  # 2

    distances = {p1: 10, p3: 20}
    print(distances[p2])  # 10

    print(p1)  # Point(1, 2)
    print([p1, p3])  # [Point(1, 2), Point(3, 4)]