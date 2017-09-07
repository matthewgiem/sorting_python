def bubble_sort(arg):
    new_array = arg
    # sort
    i = 0
    x = 0
    times = 0
    for x in range(0, len(new_array) - 1):
        for i in range(0, len(new_array) - 1):
            if new_array[i] > new_array[i + 1]:
                num1 = new_array[i]
                num2 = new_array[i + 1]
                new_array[i] = num2
                new_array[i + 1] = num1
            i += 1
            times += 1
            if i == len(new_array) - x:
                break
        x += 1
    return new_array, times
