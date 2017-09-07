def insersion_sort(arg):
    new_array = arg
    # sort
    i = 0
    x = 1
    times = 0
    for x in range(1, len(new_array)):
        for i in range(0, len(new_array) - (len(new_array) - x)):
            if new_array[x - i] < new_array[x - 1 - i]:
                num1 = new_array[x - i]
                num2 = new_array[x - 1 - i]
                new_array[x - i] = num2
                new_array[x - 1 - i] = num1
            i += 1
            times += 1
            if new_array[x - i] >= new_array[x - 1 - i]:
                break
        x += 1
    return new_array, times
