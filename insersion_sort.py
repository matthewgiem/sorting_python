def insersion_sort(arg):
    array = list(arg)
    times = 0
    swaps = 0
    i = 0
    for x in range(len(array) - 1):
        for i in range(x - i, -1, -1):
            # if len(array) == 10:
            #     print("i = {}".format(i))
            #     print("x = {}".format(x))
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
            # if len(array) == 10:
            #     print(array)
            times += 1
    return array, times, "Insertion Sort", swaps, arg
