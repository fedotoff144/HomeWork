"""
- Добавьте к задаче логирование ошибок и полезной информации.
- Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import logging
import argparse

FORMAT = '{levelname:<6}-  {asctime}, line {lineno:03d}. Status: {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='log_task_03.log',
                    filemode='a', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger('task_03.py')


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2

    def __str__(self):
        return f'class: Bird, wingspan: {self.wingspan}'

    def __repr__(self):
        return f'Bird({self.name}, {self.wingspan})'


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'

    def __str__(self):
        return f'class: Fish, max_depth: {self.max_depth}'

    def __repr__(self):
        return f'Fish({self.name}, {self.max_depth})'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return 'Обычный'

    def __str__(self):
        return f'class: Mammal, weight: {self.weight}'

    def __repr__(self):
        return f'Mammal({self.name}, {self.weight})'


class AnimalFactory:
    def create_animal(animal_type: str, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')


def parse():
    try:
        parser = argparse.ArgumentParser(description='Task for intermediate certification',
                                         prog='AnimalFactory',
                                         epilog='Return needed class [Bird, Fish, Mammal]')
        parser.add_argument('-cn', '--class_name', metavar='CLASS_NAME', type=str, nargs=1,
                            help='Enter class name which you want to get.')
        parser.add_argument('-an', '--animal_name', metavar='ANIMAL_NAME', type=str, nargs=1,
                            help='Enter the name of the animal.')
        parser.add_argument('-p', '--property', metavar='PROPERTY', type=int, nargs=1,
                            help='Enter the property of the animal')
        args = parser.parse_args()
        new_instance = AnimalFactory.create_animal(args.class_name[0], args.animal_name[0],
                                                   args.property[0])
        logger.debug(f'OK. {new_instance}')
        return new_instance
    except Exception as e:
        logger.error(f'ERROR! {e}')


if __name__ == '__main__':
    print('OK...' if parse() else 'ERROR!')

# command for run
# python task_03.py -cn Fish -an Nemo -p 101
