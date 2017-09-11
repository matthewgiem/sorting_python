def optimized_bubble_sort(arg):
    array = list(arg)
    swaps = 0
    times = 0
    for x in range(len(array)):
        exit = True
        for i in range(len(array) - 1 - x):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
                exit = False
            times += 1
        if exit:
            break
    return array, times, "Optimized Bubble Sort", swaps, arg
