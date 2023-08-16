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
import math

fraction_a = input('Введите первую дробь в формате a/b: ')
fraction_b = input('Введите вторую дробь в формате a/b: ')

a = fraction_a.split('/')
b = fraction_b.split('/')


def simple_fraction(numerator: int, denominator: int) -> str:
    gcd = math.gcd(numerator, denominator)
    if numerator // gcd == denominator // gcd:
        return f"{numerator // gcd}"
    else:
        return f"{numerator // gcd}/{denominator // gcd}"


# fractions sum

numerator_sum = int(a[0]) * int(b[1]) + int(a[1]) * int(b[0])
denominator_sum = int(a[1]) * int(b[1])

print(f"Сумма дробей: {simple_fraction(numerator_sum, denominator_sum)}")
print(f'Проверка: {fractions.Fraction(fraction_a) + fractions.Fraction(fraction_b)}')


# fractions multiplication

numerator_mult = int(a[0]) * int(b[0])
denominator_mult = int(a[1]) * int(b[1])

print(f"Произведение дробей: {simple_fraction(numerator_mult, denominator_mult)}")
print(f'Проверка: {fractions.Fraction(fraction_a) * fractions.Fraction(fraction_b)}')
