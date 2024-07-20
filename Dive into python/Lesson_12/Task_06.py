"""
Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Range:
    def __init__(self, min_val: int = None, max_val: int = None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError('Invalid data type')
        if self.min_val is not None and value <= self.min_val:
            raise ValueError(f'Values less than {self.min_val}')
        if self.max_val is not None and value <= self.max_val:
            raise ValueError(f'Values bigger than {self.max_val}')


class Rectangle:
    __slots__ = ('_a', '_b')

    a = Range(0)
    b = Range(0, 10)

    def __init__(self, a, b=None):
        self._a = a
        self._b = b if b else a

    def square(self):
        return self._a * self._b

    def perimetr(self):
        return 2 * self._a + 2 * self._b


if __name__ == '__main__':
    rect_1 = Rectangle(4)
    rect_2 = Rectangle(-1, 20)

    print(rect_1.square())
    print(rect_2.square())
