"""
Напишите функцию для транспонирования матрицы transposed_matrix, принимает
в аргументы matrix, и возвращает транспонированную матрицу.

Пример

На входе:
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transposed_matrix = transpose(matrix)

На выходе:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transpose(matrix):
    if len(matrix) == 1:
        return matrix
    result = []
    length_element = len(matrix[1])
    for i in range(length_element):
        temp_lst = [line[i] for line in matrix]
        result.append(temp_lst)
    return result


transposed_matrix = transpose(matrix)
print(transposed_matrix)
