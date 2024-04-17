# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
#
# *Верните все возможные варианты комплектации рюкзака.


load_capacity = int(input('Enter backpack weight: '))
my_stuff = {'rope': 3, 'pan': 5, 'tent': 10, 'plate': 1,
            'cup': 1, 'pillow': 4, 'towel': 2, 'laptop': 7,
            'kettle': 3, 'pot': 4, 'blanket': 3, 'water': 5}
result_list: list = []

# Сортируем словарь с вещами по весу
sorted_my_stuff = dict(sorted(my_stuff.items(), key=lambda x: x[1], reverse=True))

# Запускаем цикл с добавлением элементов в список варианта с последующим добавлением варианта в результрующий список
while len(my_stuff) > 0:
    temp_list: list = []
    temp_capacity = load_capacity

    for key, item in sorted_my_stuff.items():
        if temp_capacity - item >= 0 and key in my_stuff:
            temp_list.append(key)
            temp_capacity -= item
            my_stuff.pop(key)
    result_list.append(temp_list)

# Выводим на печать результирующий список
for i, _ in enumerate(result_list, 1):
    print(f'Список {i}: {_}')

