import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.is_triangle = self.check_triangle()
        self.perimeter = self.side_a + self.side_b + self.side_c
        self.area = math.sqrt(
            self.perimeter*(self.perimeter-self.side_a)*(self.perimeter-self.side_b)*(self.perimeter-self.side_c)
        )

    def check_triangle(self):
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError("3 sides of triangle must be greater than 0")
        if self.side_a + self.side_b > self.side_c:
            return True
        if self.side_a + self.side_c > self.side_b:
            return True
        if self.side_b + self.side_c > self.side_a:
            return True
        else:
            raise ValueError("2 sides of triangle must be greater than other side")
