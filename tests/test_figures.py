import math

import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestFigures:
    def test_circle_area(self):
        c = Circle(5)
        assert c.area == math.pi * 5 ** 2

    def test_circle_perimeter(self):
        c = Circle(5)
        assert c.perimeter == 2 * math.pi * 5

    def test_circle_add_area(self):
        c = Circle(5)
        c1 = Circle(10)
        area_sum = c.add_area(c1)
        assert area_sum == c.area + c1.area

    def test_square_area(self):
        s = Square(5)
        assert s.area == 5 * 5

    def test_square_perimeter(self):
        s = Square(5)
        assert s.perimeter == 5 * 4

    def test_square_add_area(self):
        s = Square(5)
        s1 = Square(10)
        area_sum = s.add_area(s1)
        assert area_sum == s.area + s1.area

    def test_rectangle_area(self):
        c = Rectangle(5, 10)
        assert c.area == 5 * 10

    def test_rectangle_perimeter(self):
        c = Rectangle(5, 10)
        assert c.perimeter == 5 * 2 + 10 * 2

    def test_rectangle_add_area(self):
        c = Rectangle(5, 10)
        c1 = Rectangle(10, 20)
        area_sum = c.add_area(c1)
        assert area_sum == c.area + c1.area

    def test_triangle_area(self):
        s = Triangle(3, 4, 5)
        perimeter = 3+4+5
        assert s.area == math.sqrt(
            perimeter*(perimeter-3)*(perimeter-4)*(perimeter-5)
        )

    def test_triangle_perimeter(self):
        s = Triangle(3, 4, 5)
        assert s.perimeter == 3 + 4 + 5

    def test_triangle_add_area(self):
        s = Triangle(3, 4, 5)
        s1 = Triangle(4, 5, 6)
        area_sum = s.add_area(s1)
        assert area_sum == s.area + s1.area
