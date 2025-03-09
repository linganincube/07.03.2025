class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate_area(self):
        super().calculate_area()
        return self.width * self.height

# Usage example
rectangle = Rectangle(14, 10)
area = rectangle.calculate_area()
print(area)  # Output: 50

