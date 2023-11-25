# quick sort by recursion

unsort_arr = [4,2,5,1,6,3,0]


def quick_sort(arr:list)->list:
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less_arr = [i for i in arr[1:] if i <= pivot]
    greater_arr = [i for i in arr[1:] if i > pivot]
    return quick_sort(less_arr) + [pivot] + quick_sort(greater_arr)
    
    
print(quick_sort(unsort_arr))