# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Enter number: '))
MESSAGE = ''
MAX_LIMIT = 100_000
MIN_LIMIT = 0

if num <= MIN_LIMIT or MAX_LIMIT <= num:
    MESSAGE = 'Number outside, re-enter!'
elif num == 1:
    MESSAGE = '1 is not prime and not composite number'
elif (num != 2 and num != 3 and num != 5) and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
    MESSAGE = 'Number is composite'
else:
    MESSAGE = 'Number is prime'

print(MESSAGE)
