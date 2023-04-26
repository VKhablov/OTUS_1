from src.Figure import Figure


class Square(Figure):
    def __init__(self, side_1):
        self.side = side_1
        self.is_square = self.check_square()
        self.area = self.side ** 2
        self.perimeter = self.side * 4

    def check_square(self):
        if self.side > 0:
            return True
        else:
            raise ValueError("Sides must be greater than 0")
