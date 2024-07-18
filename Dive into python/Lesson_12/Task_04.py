"""
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:

    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b else a

    def square(self):
        return self.a * self.b

    def perimetr(self):
        return 2 * self.a + 2 * self.b


if __name__ == '__main__':
    rect_1 = Rectangle(4)
    rect_2 = Rectangle(2, 7)
    print(rect_1.square(), rect_1.perimetr())
    print(rect_2.square(), rect_2.perimetr())
