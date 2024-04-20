"""
Напишите функцию для транспонирования матрицы.
Пример: [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]

"""

list_a = [1, 2, 3]
list_b = [4, 5, 6]
result = []


def matrix_transpose(data_a: list, data_b: list, res: list) -> list:
    for i in range(len(data_a)):
        temp_list = [data_a[i], data_b[i]]
        res.append(temp_list)

    return res


print(matrix_transpose(list_a, list_b, result))
