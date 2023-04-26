from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.is_rectangle = self.check_rectangle()
        self.area = self.width * self.height
        self.perimeter = self.width * 2 + self.height * 2

    def check_rectangle(self):
        if self.width > 0 and self.height > 0:
            return True
        else:
            raise ValueError("Width and height must be greater than 0")