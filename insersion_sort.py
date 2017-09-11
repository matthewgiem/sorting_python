def insersion_sort(arg):
    array = list(arg)
    times = 0
    swaps = 0
    for x in range(len(array)):
        for i in range(len(array) - 1):
            times += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
                for j in range(x):
                    times += 1
                    if array[i] > array[i - j]:
                        array[i], array[i - j] = array[i - j], array[i]
                        swaps += 1
                    else:
                        break
    return array, times, "Insertion Sort", swaps
