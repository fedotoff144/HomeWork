# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]


my_list = [1, 2, 3, 1, 2, 4, 5]
new_list = []

for i in my_list:
    count = my_list.count(i)
    if count > 1:
        if i not in new_list:
            new_list.append(i)

print(new_list)
