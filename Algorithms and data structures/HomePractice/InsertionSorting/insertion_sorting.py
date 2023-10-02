# Insertion sorting

my_arr = [9, 2, 5, 4, 8, 6, 3, 1, 7]
arr_sorted = []


def find_min(arr, arr_sort):
    min = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    arr.pop(index)
    arr_sort.append(min)


def arr_sort(arr, arr_sort):
    while True:
        if len(arr) != 0:
            find_min(arr, arr_sort)
        else:
            break


arr_sort(my_arr, arr_sorted)
print(f'{my_arr = }\n{arr_sorted = }')
