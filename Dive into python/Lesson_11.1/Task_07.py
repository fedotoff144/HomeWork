"""
Задание
- Решить задачи, которые не успели решить на семинаре.
- Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать.
- Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""


class Matrix:
    """Represents a matrix with dimensions specified by side_a and side_b."""
    def __init__(self, side_a: int, side_b=None):
        """Initializes a new instance of the Matrix class."""
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def __str__(self):
        """Returns a string representation of the Matrix instance."""
        generator = ''.join('\n' + '*' * self._side_a for _ in range(self._side_b))
        return f'Instance class Matrix, {self._side_a} x {self._side_b}{generator}'

    def __repr__(self):
        """Provides a string that represents the Matrix instance for debugging purposes."""
        return f'Matrix({self._side_a}, {self._side_b})'

    def __eq__(self, other):
        """Compares the volumes of two Matrix instances."""
        return self.volume() == other.volume()

    def __ne__(self, other):
        """Compares the volumes of two Matrix instances for inequality."""
        return self.volume() != other.volume()

    def __gt__(self, other):
        """Compares the volumes of two Matrix instances for greater than."""
        return self.volume() > other.volume()

    def __ge__(self, other):
        """Compares the volumes of two Matrix instances for greater than or equal to."""
        return self.volume() >= other.volume()

    def __lt__(self, other):
        """Compares the volumes of two Matrix instances for less than."""
        return self.volume() < other.volume()

    def __le__(self, other):
        """Compares the volumes of two Matrix instances for less than or equal to."""
        return self.volume() <= other.volume()

    def __add__(self, other):
        """Adds two Matrix instances by increasing their dimensions."""
        side_a = self._side_a + other._side_a
        side_b = self._side_b + other._side_b
        return Matrix(side_a, side_b)

    def __mul__(self, other):
        """Multiplies two Matrix instances by increasing their dimensions."""
        side_a = self._side_a * other._side_a
        side_b = self._side_b * other._side_b
        return Matrix(side_a, side_b)

    def volume(self):
        """Calculates the volume of the Matrix instance."""
        return self._side_a * self._side_b


matrix1 = Matrix(5)
matrix2 = Matrix(4)

print(matrix1)
print(matrix2)

print(matrix1 + matrix2, '\n', matrix1 * matrix2)
