# find max element in list by recursion

my_arr = [5, 9, 1, 3, 6, 8, 16, 11, 4, 7, 10]
max_element = my_arr[0]


def find_max(arr: list):
    global max_element
    if len(arr) != 0:
        if arr[-1] > max_element:
            max_element = arr[-1]
        arr.pop()
        return find_max(arr)


find_max(my_arr)
print(max_element)
