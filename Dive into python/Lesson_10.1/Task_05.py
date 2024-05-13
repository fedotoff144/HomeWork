"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

Доработайте задачу.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
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


fish = Fish('Gold', 'Flipper')
bird = Bird(True, 'Kesha')
reptile = Reptile(True, 'Alligator', True)

print(fish.output_info())
print(bird.output_info())
print(reptile.output_info())
