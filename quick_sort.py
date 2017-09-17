import random
def quick_sort(arg):
    array = list(arg[0])
    type_of_data = arg[1]
    times = 0
    swaps = 0
    # pick partition
    partition = random.randint(0,len(array) - 1)
    print("partition = {}".format(array[partition]))
    less = []
    greater = []
    for i in range(len(array)):
        print(array[i])
        if i != partition:
            if array[i] >= array[partition]:
                greater.append(array[i])
            else:
                less.append(array[i])
    print(less, array[partition], greater)


    return array, times, "Quick Sort", swaps, arg[0], type_of_data
