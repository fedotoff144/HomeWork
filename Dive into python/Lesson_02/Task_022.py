# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
#
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6

import fractions

first_fraction = input('Введите первую дробь в формате a/b: ')
second_fraction = input('Введите вторую дробь в формате a/b: ')

split_first_fraction = first_fraction.split('/')
split_second_fraction = second_fraction.split('/')

first_fraction_module = fractions.Fraction(first_fraction)
second_fraction_module = fractions.Fraction(second_fraction)

print('Решение:')

# умножение дробей
numerator = int(split_first_fraction[0]) * int(split_second_fraction[0])
denominator = int(split_first_fraction[1]) * int(split_second_fraction[1])

print(f'{first_fraction} * {second_fraction} = {numerator}/{denominator}')

# сложение дробей
numerator = (int(split_first_fraction[0]) * int(split_second_fraction[1]) +
             int(split_first_fraction[1]) * int(split_second_fraction[0]))
denominator = int(split_first_fraction[1]) * int(split_second_fraction[1])

print(f'{first_fraction} + {second_fraction} = {numerator}/{denominator}')

# решение с помощью модуля fractions
print(f'Решение с помощью модуля fractions:')
print(
    f'{first_fraction} * {second_fraction} = {first_fraction_module * second_fraction_module}\n'
    f'{first_fraction} + {second_fraction} = {first_fraction_module + second_fraction_module}')
