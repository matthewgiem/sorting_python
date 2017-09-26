import random

def new_quick_sort(arg):
    type_of_data = arg[1]
    array = list(arg[0])
    print(array)
    # print(quick_sort2(array, 0, len(array) - 1))
    print(quick_sort2(array, 4, 15))

def quick_sort2(array, low, high):
    # print("array = {}, low = {}, high = {}".format(array, low, high))
    # print(range(low, high + 1))
    j = low
    for i in range(low, high + 1):
        if array[i] <= array[high]:
            array[i], array[j] = array[j], array[i]
            j += 1

    return array
