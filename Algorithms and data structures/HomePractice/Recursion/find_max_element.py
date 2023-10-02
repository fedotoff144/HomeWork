# find max element in list

my_arr = [5, 9, 1, 3, 6, 8, 2, 11, 4, 7, 12]
max_element = 0
count = 0


def find_max(max_el: int, count: int, arr: list):
    if count < len(arr):
        if arr[count] > max_el:
            max_el = arr[count]
        count += 1
        return find_max(max_el, count, arr)
    return max_el


print(find_max(max_element, count, my_arr))
