"""
На вход подается словарь со списком вещей для похода в качестве ключа и
их массой max_weight в качестве значения. Определите какие вещи влезут в рюкзак
backpack передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и
сохранен в переменную backpack. Достаточно получить один допустимый вариант
и сохранить в переменную backpack. Не выводите backpack на экран.

Пример

На входе:
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

На выходе, например, один из допустимых вариантов может быть таким:
{'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}
"""
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
MAX_WEIGHT = 1.0
result_lst = []
copy_items = items.copy()

for key in items.keys():
    check_weight = MAX_WEIGHT
    temp_dict = {}

    for sec_key, sec_value in copy_items.items():
        if check_weight - copy_items[sec_key] >= 0:
            temp_dict[sec_key] = sec_value
            check_weight -= copy_items[sec_key]
    copy_items.pop(key)
    result_lst.append(temp_dict)

for i in result_lst:
    print(i)
