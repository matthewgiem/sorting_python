import random
def quick_sort(arg):
    array = list(arg[0])
    type_of_data = arg[1]
    times = 0
    swaps = 0
    # pick partition
    partition = random.randint(0,len(array) - 1)
    # print("partition = {}".format(array[partition]))
    less = []
    greater = []
    for i in range(len(array)):
        if i != partition:
            if array[i] >= array[partition]:
                greater.append(array[i])
            else:
                less.append(array[i])
    less.append(array[partition])
    new_array = less + greater
    # print(type(less))
    # print(type(array[partition]))
    # print(less)
    # print(array[partition])
    # print(greater)
    # print("{} + {} = {}".format(less, array[partition], less.append(array[partition])))

    # answer = less.append(array[partition]) + greater
    # print(answer)

    return new_array, times, "Quick Sort", swaps, arg[0], type_of_data
