def insertion_sort(arg):
    array = list(arg[0])
    times = 0
    swaps = 0
    type_of_data = arg[1]
    for x in range(len(array) - 1):
        for i in range(x, -1, -1):
            # print(array)
            # if len(array) == 10:
            #     print("i = {}".format(i))
            #     print("x = {}".format(x))
            # print(array[i], array[i + 1])
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
                # print("swap")
            # if len(array) == 10:
            #     print(array)
            times += 1
    return array, times, "Insertion Sort", swaps, arg[0], type_of_data