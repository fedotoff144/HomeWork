"""
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""


class Factorial:
    def __init__(self, k: int = 1):
        self.k = k
        self.memory = []

    def __call__(self, num: int = 1):
        if num <= 0:
            raise ValueError('Num less or equal 0.')
        else:
            temp = 1
            for i in range(2, num + 1):
                temp *= i
                self.memory.append(temp)
                if len(self.memory) > self.k:
                    self.memory.pop(0)

    def get_memory(self):
        return self.memory


if __name__ == '__main__':
    f1 = Factorial(3)
    f1(5)
    print(f1.get_memory())