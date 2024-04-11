# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

message = None

num = int(input("Enter a positive number up to 100_000: "))

if (num < 100000) and (num > 0):
    if num == 1:
        message = 'The number is neither prime nor composite'
    elif (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
        message = 'The number is composite'
else:
    message = 'The number is prime'

print(message)
