# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
#
# *Верните все возможные варианты комплектации рюкзака.


my_stuff = {'rope': 3, 'pan': 5, 'tent': 10, 'plate': 1,
            'cup': 1, 'pillow': 4, 'towel': 2, 'laptop': 7,
            'kettle': 3, 'pot': 4, 'blanket': 3, 'water': 5}

# сортируем словарь для наиболее эффективной компановки
my_stuff_sort = dict(sorted(my_stuff.items(), reverse=True, key=lambda x: x[1]))

# создаем общий список с возможными комбинациями
total_list = []


def find_combination(load_capacity: int):
    while 1:
        if my_stuff_sort:
            temp_list = []
            total_weight = 0

            for item, weight in my_stuff_sort.items():
                if total_weight + weight <= load_capacity:
                    temp_list.append(item)
                    total_weight += weight

            total_list.append(temp_list)

            for item in temp_list:
                if item in my_stuff_sort.keys():
                    my_stuff_sort.__delitem__(item)

        else:
            break

    for elem in total_list:
        print(elem)


find_combination(15)
