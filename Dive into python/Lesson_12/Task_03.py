"""
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class Generator:

    def __init__(self, *args):
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        else:
            self.start = 1
            self.stop = args[0]
            self.step = 1
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            self.result *= self.start
            self.start += self.step
            return self.result
        else:
            return 'Out of range'


if __name__ == '__main__':
    my_gen = Generator(2, 14, 3)
    print(my_gen.__next__())
    print(my_gen.__next__())
    print(my_gen.__next__())
    print(my_gen.__next__())
    print(my_gen.__next__())
    print(my_gen.__next__())
    print(my_gen.__next__())
