"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
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