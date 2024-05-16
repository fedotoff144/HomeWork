"""
Задание №5
- Дорабатываем класс прямоугольник из прошлого семинара.
- Добавьте возможность сложения и вычитания.
- При этом должен создаваться новый экземпляр
прямоугольника.
- Складываем и вычитаем периметры, а не длину и ширину.
- При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    """
    The Rectangle class represents a rectangle with a specified length and width.
    If no width is provided, it defaults to a square with the provided length.
    """

    def __init__(self, length, width=None):
        """
        Method initializes an instance of the Rectangle class with the provided
        length and width. If no width is provided, it defaults to a square
        with the provided length.
        """
        self.length = length
        self.width = width if width else length

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance,
        displaying its length and width.
        """
        return f'length: {self.length}\twidth: {self.width}'

    def __repr__(self):
        """Returns the official string representation of the Rectangle instance."""
        return f'Rectangle({self.length}, {self.width})'

    # def __add__(self, other):
    #     """
    #     Returns a new Rectangle instance. The length and width of the new
    #     instance are the sums of the lengths and widths of the current and
    #     another Rectangle instance, respectively.
    #     """
    #     length = self.length + other.length
    #     width = self.width + other.width
    #     return Rectangle(length, width)

    def __add__(self, other):
        """
        Returns the sum of the perimeters of the current Rectangle instance
        and another Rectangle instance.
        """
        return self.perimeter() + other.perimeter()

    # def __sub__(self, other):
    #     """
    #     Method returns a new Rectangle instance. The length and width of the
    #     new instance are the differences of the lengths and widths of the
    #     current and another Rectangle instance, respectively. If either the
    #     length or the width is negative, it returns a message indicating that
    #     negative results are not allowed.
    #     """
    #     length = self.length - other.length
    #     width = self.width - other.width
    #     if length < 0 or width < 0:
    #         return 'Minus is not allowed'
    #     return Rectangle(length, width)

    def __sub__(self, other):
        """
        Returns the difference of the perimeters of the current Rectangle
        instance and another Rectangle instance. If the result is negative,
        it returns a message indicating that negative results are not allowed.
        """
        result = self.perimeter() - other.perimeter()
        if result < 0:
            return 'Minus is not allowed'
        return result

    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle instance."""
        return (self.length + self.width) * 2

    def area_rectangle(self):
        """Calculates and returns the area of the Rectangle instance."""
        return self.length * self.width


rect1 = Rectangle(5, 10)
rect2 = Rectangle(5, 10)
print(rect1 + rect2)
print(rect1 - rect2)
