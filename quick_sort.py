import random
# from return_median_of_3 import return_median_of_3
def quick_sort(arg):
    array = list(arg[0])
    type_of_data = arg[1]
    times = 0
    swaps = 0
    # pick partition
    partition = random.randint(0,len(array) - 1)
    partition_options = random.sample(range(0, len(array)), 3)

    less = []
    greater = []
    for i in range(len(array)):
        if i != partition:
            if array[i] >= array[partition]:
                greater.append(array[i])
            else:
                less.append(array[i])
    less.append(array[partition])
    array = less + greater


    return array, times, "Quick Sort", swaps, arg[0], type_of_data
