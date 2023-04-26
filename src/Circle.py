import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius
        self.is_circle = self.check_circle()
        self.area = math.pi * self.radius ** 2
        self.perimeter = 2 * math.pi * self.radius

    def check_circle(self):
        if self.radius > 0:
            return True
        else:
            raise ValueError("Radius must be greater than 0")


if __name__ == "__main__":
    c = Circle(0)
    print(c.is_circle)
