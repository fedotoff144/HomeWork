# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
#
# *Верните все возможные варианты комплектации рюкзака.

my_stuff = {'rope': 3, 'pan': 5, 'tent': 10, 'plate': 1,
            'cup': 1, 'pillow': 4, 'towel': 2, 'laptop': 7,
            'kettle': 3, 'pot': 4, 'blanket': 3, 'water': 5}


def max_weight(load_capacity: int) -> list:
    backpack = []
    total_weight = 0
    for item, weight in my_stuff.items():
        if total_weight + weight <= load_capacity:
            backpack.append(item)
            total_weight += weight
    return backpack


print(max_weight(10))
