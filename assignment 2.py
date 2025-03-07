from math import pi


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate total area of a list of shapes
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

# Example usage
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Circle(3),
        Rectangle(2, 3)
    ]

    total = total_area(shapes)
    print(f"Total area of all shapes: {total}")