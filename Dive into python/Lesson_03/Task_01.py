# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]


my_list = [1, 2, 3, 1, 2, 4, 5]
res = []

for elem in my_list:
    if my_list.count(elem) > 1 and elem not in res:
        res.append(elem)

print(res)