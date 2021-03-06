def optimized_insertion_sort(arg):
    array = list(arg[0])
    type_of_data = arg[1]
    times = 0
    swaps = 0
    for x in range(len(array) - 1):
        for i in range(x, -1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
            else:
                break
            times += 1
    return array, times, "Optimized Insertion Sort", swaps, arg[0], type_of_data
