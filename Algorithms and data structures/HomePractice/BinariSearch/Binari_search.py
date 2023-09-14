my_arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
guess = int(input('enter number: '))


def find_binary(arr: list, num) -> str:
    # indexes
    min = 0
    max = len(arr) - 1
    mid = (min + max) // 2

    while True:
        if arr[mid] != num:
            if num < arr[mid]:
                max = mid
            else:
                min = mid

            mid = (min + max) // 2
        else:
            return f'index of num guess={mid}, your num={arr[mid]}'


print(find_binary(my_arr, guess))