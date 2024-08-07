"""
Напишите код, который анализирует число num и сообщает является ли оно простым
или составным. Используйте правило для проверки: “Число является простым,
если это число натуральное и делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
Если подается отрицательное число или число более ста тысяч, выведите на экран
сообщение: "Число должно быть больше 1 и меньше 100000".

Внимание! Число 1 — не является ни простым, ни составным числом, так как у него
только один делитель — 1.

Пример
На входе:
num = 2

На выходе:
Простое

На входе:
num = 1000001

На выходе:
Не является простым
"""

num = 99999  

if 1 < num <= 100_000:
    if (num == 2 or num == 3 or num == 5) or (
            num % 2 != 0 and num % 3 != 0 and num % 5 != 0):
        message = 'Простое'
    else:
        message = 'Не является простым'
else:
    message = 'Число должно быть больше 1 и меньше 100000'

print(message)
