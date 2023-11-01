# Insertion sorting

my_arr = [9, 2, 5, 4, 8, 6, 3, 1, 7]
arr_sorted = []


def find_min(unsort_arr, sorted_arr):
    min_element = unsort_arr[0]
    index = 0
    for i in range(len(unsort_arr)):
        if unsort_arr[i] < min_element:
            min_element = unsort_arr[i]
            index = i
    unsort_arr.pop(index)
    sorted_arr.append(min_element)


def arr_sort(unsort_arr, sorted_arr):
    while True:
        if len(unsort_arr) != 0:
            find_min(unsort_arr, sorted_arr)
        else:
            break


print(f'initiol list: {my_arr}')
arr_sort(my_arr, arr_sorted)
print(f'sorted list: {arr_sorted}')
