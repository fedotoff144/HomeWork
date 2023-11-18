my_arr = [0,1,2,3,4,5,6]
n = int(input("enter your number: "))
min_index = 0
max_index = len(my_arr)-1
middle = len(my_arr)//2


def find_num(min_index:int, middle:int, max_index:int, arr:list):
  global n
  if n > arr[middle]:
    min_index = middle
    middle = (max_index - min_index + 1)//2 + min_index
    return find_num(min_index, middle, max_index, arr)
  if n < arr[middle]:
    max_index = middle
    middle = (max_index - min_index)//2 + min_index
    return find_num(min_index, middle, max_index, arr)
  return middle


print(f"{my_arr=}")
print(f"index of your number in array: {find_num(min_index,middle,max_index,my_arr)}")