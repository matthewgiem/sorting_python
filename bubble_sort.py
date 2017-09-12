def bubble_sort(arg):
    array = list(arg[0])
    type_of_data = arg[1]
    swaps = 0
    times = 0
    for x in range(len(array)):
        for i in range(len(array) - 1 - x):
            # if len(array) == 10:
            #     print("i = {}".format(i))
            #     print("x = {}".format(x))
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
                exit = False
            # if len(array) == 10:
            #     print(array)
            times += 1
    return array, times, "Bubble Sort", swaps, arg[0], type_of_data
