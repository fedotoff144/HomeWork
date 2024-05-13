"""
Задача 1.
Решить задания, которые не успели решить на семинаре.

Задача 2.
Доработаем заданиe 5. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

Задача 3.
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.Задача
"""


class Animal:
    def __init__(self, name, is_predator=False):
        self.name = name
        self.is_predator = is_predator

    def output_info(self):
        return f'name: {self.name}, is predator: {self.is_predator}'


class Fish(Animal):
    def __init__(self, color, *args, **kwargs):
        self.color = color
        super().__init__(*args, **kwargs)

    def output_info(self):
        return f'name: {self.name}, is predator: {self.is_predator}, color: {self.color}'


class Bird(Animal):
    def __init__(self, flying, *args, **kwargs):
        self.flying = flying
        super().__init__(*args, **kwargs)

    def output_info(self):
        return f'name: {self.name}, is predator: {self.is_predator}, flying: {self.flying}'


class Reptile(Animal):
    def __init__(self, poisonous, *args, **kwargs):
        self.poisonous = poisonous
        super().__init__(*args, **kwargs)

    def output_info(self):
        return f'name: {self.name}, is predator: {self.is_predator}, poisonous: {self.poisonous}'


class AnimalFactory:
    def identify_class(type_class, *args, **kwargs):
        if type_class == Fish:
            return Fish(*args, **kwargs)
        if type_class == Bird:
            return Bird(*args, **kwargs)
        if type_class == Reptile:
            return Reptile(*args, **kwargs)


fish = Fish('Gold', 'Flipper')
bird = Bird(True, 'Kesha')
reptile = Reptile(True, 'Alligator', True)

some_animal = AnimalFactory.identify_class(Reptile, False, 'Kaa', False)
print(some_animal.output_info())
