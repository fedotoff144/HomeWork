"""
Напишите функцию для транспонирования матрицы.
Пример: [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]

"""

first_list = [1, 2, 3]
second_list = [4, 5, 6]
total_list = []

for el_frst_list, el_scnd_list in zip(first_list, second_list):
    total_list.append([el_frst_list, el_scnd_list])

print(total_list)
