import random
from numpy import median

def new_quick_sort(arg):
    type_of_data = arg[1]
    array = list(arg[0])
    print(array)
    print(quick_sort2(array, 0, len(array) - 1))
    # print(quick_sort2(array, 4, 15))

def quick_sort2(array, low, high):
    j = low
    partition = array.index(int(median(random.sample(array[low:high], 3))))
    array[-1], array[partition] = array[partition], array[-1]
    for i in range(low, high + 1):
        if i == high:
            partition = j
        if array[i] <= array[high]:
            array[i], array[j] = array[j], array[i]
            j += 1
    return array, partition
