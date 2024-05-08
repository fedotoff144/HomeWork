"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from typing import Callable


def decorator(func: Callable):
    def wrapper():
        counter = int(input('Enter number of attempts from 1 to 10: '))
        for _ in range(counter):
            num = int(input('Enter guess number from 1 to 100: '))
            flag = func(num)
            if flag:
                return 'You win!'
            print('No')
        return 'You lose...'

    return wrapper


# @decorator
def guess_num(num_guess):
    goal = 8
    if num_guess == goal:
        return 1


# print(guess_num())

decor = decorator(guess_num)
print(decor())