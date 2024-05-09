"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.

Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
import random
from typing import Callable

SECRET_NUM = 8


def decorator(func: Callable):
    counter = int(input('Enter number of attempts from 1 to 10: '))
    num = int(input('Enter guess number from 1 to 100: '))

    def wrapper(*args):
        lst_args = list(args)
        if 10 < lst_args[1] or args[1] < 1:
            lst_args[1] = random.randint(1, 10)
            print(f'{args[1]} is out of range so attempts: {lst_args[1]}')
        if 100 < lst_args[0] or lst_args[0] < 1:
            lst_args[0] = random.randint(1, 100)
            print(f'{args[0]} is out of range so number is: {lst_args[0]}')
        return func(*lst_args)

    return wrapper(num, counter)


# @decorator
def guess_num(num_guess, count):
    for _ in range(count - 1):
        if num_guess == SECRET_NUM:
            return 'You win!'
        print('No')
        num_guess = int(input('Enter guess number from 1 to 100: '))
    return 'You lose...'


# print(guess_num())

decor = decorator(guess_num)
print(decor)
