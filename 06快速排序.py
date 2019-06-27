#两种排序方法的速度对比
import random
import time, timeit
#快速排序
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

#选择排序
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if(arr[i]<smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr




arr = []

while len(arr)<=50000:
    arr.append(random.randint(1,10000))

timer1 = timeit.default_timer()
print(quicksort(arr))
timer2 = timeit.default_timer()

timer3 = timeit.default_timer()
print(selectionSort(arr))
timer4 = timeit.default_timer()


print(timer2-timer1)
print(timer4-timer3)