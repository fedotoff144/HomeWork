"""
Напишите функцию принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента.Если ключ не хешируем,
используйте его строковое представление.
Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

"""


def function(**kwargs) -> dict:
    result = {}
    for key, value in kwargs.items():
        value = str(value)
        result[value] = key
    return result


print(function(res=1, reverse=[1, 2, 3]))
