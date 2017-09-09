def bubble_sort(arg):
    array = list(arg)
    # sort
    swaps = 0
    times = 0
    for x in range(len(array)):
        for i in range(len(array) - 1 - x):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
            times += 1
            # if i == len(array) - x:
            #     break
    return array, times, "Bubble Sort", swaps
