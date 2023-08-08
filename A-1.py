from abc import ABC, abstractmethod


class Shape(ABC):
    # An abstract base class for shapes.

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        pass

    # Single Responsibility Principle (SRP).

    def _get_area(self):
        return self.width * self.height


class Rectangle(Shape):

    # Open-Closed Principle (OCP).

    def __init__(self, width, height):
        super().__init__(width, height)

    # Liskov Substitution Principle (LSP).

    def area(self):
        return self._get_area()


class Square(Rectangle):

    # Interface Segregation Principle (ISP).

    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    # Dependency Inversion Principle (DIP)

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    rectangle = Rectangle(20, 30)
    print(rectangle.area())

    square = Square(15)
    print(square.area())
