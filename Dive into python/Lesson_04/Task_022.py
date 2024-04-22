"""
Напишите функцию принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента.Если ключ не хешируем,
используйте его строковое представление.
Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

"""


def convert_dict(**kwargs) -> dict:
    result: dict = {}
    for key, value in kwargs.items():
        if not value.__hash__:
            result[str(value)] = key
        else:
            result[value] = key
    return result


print(convert_dict(res=1, reverse=[1, 2, 3]))
