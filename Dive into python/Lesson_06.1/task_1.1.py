"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу,
которая проверяет, является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
в зависимости от результата проверки.

Пример использования На входе:
date_to_prove = 15.4.2023

На выходе:
True

На входе:
date_to_prove = 31.6.2022

На выходе:
False
"""
date_to_prove = '12.5.-2022'


def _is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def check_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    leap_year = _is_leap_year(year)
    if year > 0 and month > 0 and day > 0:
        if (leap_year and month == 2 and 0 < day <= 29) or \
                (not leap_year and month == 2 and 0 < day <= 28):
            return True
        if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day <= 31:
            return True
        if month in [4, 6, 9, 11] and 0 < day <= 30:
            return True
    return False


print(check_date(date_to_prove))
