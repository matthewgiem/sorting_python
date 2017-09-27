import random as rand
from numpy import median as med

def new_quick_sort(arg):
    type_of_data = arg[1]
    array = list(arg[0])
    print(array)
    quick_sort2(array, 0, len(array) - 1)
    # print(quick_sort2(array, 0, len(array) - 1))

def quick_sort2(array, low, high):
    print("inside")
    j = low
    partition = array.index(int(med(rand.sample(array[low:high], 3))))
    array[high], array[partition] = array[partition], array[high]
    for i in range(low, high + 1):
        if i == high:
            partition = j
        if array[i] <= array[high]:
            array[i], array[j] = array[j], array[i]
            j += 1
    # print("low is {}".format(low))
    # print("partition is {}".format(partition))
    if partition - low < 10:
        print("#1")
        # print("the low point is {}".format(low))
        # print("the partition is {}".format(partition))
        bubble_sort_for_quick_sort(array, low, partition)
    else:
        print("#2")
        # print("the partition is less than 10 its {}".format(partition - low))
        quick_sort2(array, low, partition - 1)
    if high - partition < 10:
        print("#3")
        bubble_sort_for_quick_sort(array, partition + 1, high)
    else:
        print("#4")
        quick_sort2(array, partition + 1, high)

    print(array)


def bubble_sort_for_quick_sort(array, low, high):
    # print("low = {}".format(low))
    # print("high = {}".format(high))
    # print("x goes between {}, and {}".format(0, high - low))
    for x in range(high - low):
        # print("x = {}".format(x))
        # print(array)
        # print("i goes between in the range of {}".format(range(low, high - x)))
        for i in range(low, high - x):
            # print("i = {}".format(i))
            # print("comparing {} and {}".format(array[i], array[i + 1]))
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                # print(array)
    return array
