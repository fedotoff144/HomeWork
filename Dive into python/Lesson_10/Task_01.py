"""
Задача 1.
Решить задания, которые не успели решить на семинаре.

Задача 2.
Доработаем задания 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

Задача 3.
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.Задача
"""


class Animal:
    type = 'animal'

    def __int__(self):
        pass

    def print_animal_info(self):
        return f'{self.type=}'


class Fish(Animal):
    name = 'fish'
    habitat = 'water'
    peculiarity = 'fins'
    gills = True

    def __int__(self, *args, **kwargs):
        super().__int__()

    def print_class_info(self):
        return f'{Animal.print_animal_info(self)=}, {self.name=}, {self.habitat=}, {self.peculiarity=}, {self.gills=}'


class Bird(Animal):
    name = 'bird'
    habitat = 'air'
    peculiarity = 'wings'
    ability_to_fly = True

    def __int__(self, *args, **kwargs):
        super().__int__()

    def print_class_info(self):
        return f'{self.type=}, {self.name=}, {self.habitat=}, {self.peculiarity=}, {self.ability_to_fly=}'


class Reptile(Animal):
    name = 'reptile'
    habitat = 'drought'
    peculiarity = 'tail'
    sharp_teeth = True

    def __int__(self):
        super().__int__()

    def print_class_info(self):
        return f'{self.type=}, {self.name=}, {self.habitat=}, {self.peculiarity=}, {self.sharp_teeth=}'


fish = Fish()
print(fish.print_class_info())
# bird = Bird()
# print(bird.print_class_info())