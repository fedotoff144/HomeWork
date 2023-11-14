my_arr = [1,2,3,4,5,6,7,8,9]
n = int(input("enter your number: "))
min_index = 0
max_index = len(my_arr)-1
middle = len(my_arr)//2


def find_num(min_index:int, middle:int, max_index:int, arr:list) -> int:
  global n
  if n != arr[middle]:
    if n > arr[middle]:
      min_index = middle
      middle = (max_index-middle)//2
      return find_num(min_index, middle, max_index, arr)
    if n < arr[middle]:
      max_index = middle
      middle = max_index//2
      return find_num(min_index, middle, max_index, arr)
  return middle


print(f"{n=}")
print(f"{my_arr=}")
print(f"index of your number in array: {find_num(min_index,middle,max_index,my_arr)}")
