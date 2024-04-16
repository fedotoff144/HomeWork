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

# Сортируем словарь с вещами и создаем список с возможными вариантами
sorted_my_stuff = dict(sorted(my_stuff.items(), key=lambda x: x[1], reverse=True))

for key, item in sorted_my_stuff.items():
    if load_capacity - item > 0:
        result_list.append(key)
        load_capacity -= item
        my_stuff.pop(key)

print(my_stuff)
print(result_list)