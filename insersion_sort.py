def insersion_sort(arg):
    # create new list not just a pointer
    array = list(arg)
    # sort
    times = 0
    swaps = 0
    for x in range(1, len(array)):
        for i in range(0, len(array) - (len(array) - x)):
            if array[x - i] < array[x - 1 - i]:
                array[x - i], array[x - 1 - i] = array[x - 1 - i], array[x - i]
                swaps += 1
            times += 1
            if array[x - i] >= array[x - 1 - i]:
                break
    return array, times, "Insertion Sort", swaps
