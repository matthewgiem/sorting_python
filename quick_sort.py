import random
from return_median_of_3 import return_median_of_3
from optimized_insertion_sort import optimized_insertion_sort
def quick_sort(arg):
    array = list(arg[0])
    type_of_data = arg[1]
    times = 0
    swaps = 0
    # pick partition
    partition_options = random.sample(range(0, len(array)), 5)
    partition_options.sort()
    partition = partition_options[2]
    # partition = return_median_of_3(array)
    # partition_options = random.sample(range(0, len(array)), 3)

    less = []
    greater = []
    for i in range(len(array)):
        if i != partition:
            if array[i] >= array[partition]:
                greater.append(array[i])
                swaps += 1
            else:
                less.append(array[i])
                swaps += 1
        times += 1
    answer_low = optimized_insertion_sort([less, "string"])
    answer_low[0].append(array[partition])
    answer_high = optimized_insertion_sort([greater, "string"])
    array = answer_low[0] + answer_high[0]
    times = times + answer_low[1] + answer_high[1]
    swaps = swaps + answer_low[3] + answer_high[3]


    return array, times, "Quick Sort", swaps, arg[0], type_of_data
