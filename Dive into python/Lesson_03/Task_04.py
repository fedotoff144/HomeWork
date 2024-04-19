# Дополнительное:
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.


data = {
    "Иван": ("нож", "палатка", "солнечные очки", "водонепроницаемая куртка"),
    "Алексей": ("телефон", "палатка", "нож"),
    "Сергей": ("палатка", "спальный мешок", "нож", "кухонные принадлежности"),
    "Вадим": ("нож", "водонепроницаемая куртка", "чашка")
}

list_sets = [set(x) for x in data.values()]

# (Объединение множеств) Множество вещей всех друзей в походе
union_sets = set()
union_sets = union_sets.union(*list_sets)
print('Все вещи которые взяли друзья в поход: ' + ', '.join(union_sets))

# (Разность множеств) Уникальные вещи каждого из друзей
print('Список друзей и их уникальные вещи:')

for i in range(len(list_sets)):
    diff_sets: set = list_sets[i]
    iterable_list = [x for j, x in enumerate(list_sets) if j != i]

    for set_ in iterable_list:
        diff_sets = diff_sets.difference(set_)

    key_diff_sets = next(k for k, v in data.items() if diff_sets & set(v))
    print(key_diff_sets + ' имеет: ' + ', '.join(diff_sets))

# (Пересечение множеств) Вещи которые есть у каждого друга
intersec_sets: set = list_sets[0]
iterable_list = [x for x in list_sets[1:]]

for set_ in iterable_list:
    intersec_sets = intersec_sets.intersection(set_)

print('Каждый из друзей взял с собой: ' + ', '.join(intersec_sets))
