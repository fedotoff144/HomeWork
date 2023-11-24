# quick sort by recursion

my_arr = [6, 3, 4, 2, 5, 1, 0]


def quick_sort(unsort_arr):
  pivot = unsort_arr[0]
  if len(unsort_arr) < 2:
    return unsort_arr
  else:
    less_arr = [i for i in unsort_arr if i[1] <= pivot]
    greater_arr = [i for i in unsort_arr if i[1] > pivot]
    return quick_sort(less_arr+unsort_arr+greater_arr)
    

print(quick_sort(my_arr))
