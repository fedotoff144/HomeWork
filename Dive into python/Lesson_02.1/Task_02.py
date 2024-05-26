"""
Задание №2
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь
с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.

Пример

На входе:
frac1 = "1/2"
frac2 = "1/3"

На выходе:
Сумма дробей: 5/6
Произведение дробей: 1/6
Сумма дробей: 5/6
Произведение дробей: 1/6
"""
import fractions

frac1 = "5/2"
frac2 = "1/3"

numerator_frac1 = int(frac1.split('/')[0])
denominator_frac1 = int(frac1.split('/')[1])
numerator_frac2 = int(frac2.split('/')[0])
denominator_frac2 = int(frac2.split('/')[1])

# sum fractions
denominator_sum = denominator_frac1 * denominator_frac2
numerator_sum = denominator_frac1 * numerator_frac2 + denominator_frac2 * numerator_frac1
result_sum = f'{numerator_sum}/{denominator_sum}'

# mult fractions
denominator_mult = denominator_frac1 * denominator_frac2
numerator_mult = numerator_frac1 * numerator_frac2
result_mult = f'{numerator_mult}/{denominator_mult}'

print(f'Сумма дробей: {result_sum}\nПроизведение дробей: {result_mult}')
print(f'Сумма дробей: {fractions.Fraction(frac1) + fractions.Fraction(frac2)}\n'
      f'Произведение дробей: {fractions.Fraction(frac1) * fractions.Fraction(frac2)}')
