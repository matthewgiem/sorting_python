def quick_sort(arg):
    unsorted_numbers = arg
    array = []
    new_array = []
    newer_array = []
    array = unsorted_numbers.split()
    for x in array:
        new_array.append(int(x))
    pick = new_array[randint(1, len(array))]
    # print(new_array[pick])
    # print(new_array)
    x = 0
    greater_than_array = []
    less_than_array = []
    for x in range(0, len(new_array)):
        if new_array[x] > new_array[pick]:
            greater_than_array.append(new_array[x])
        else:
            less_than_array.append(new_array[x])
        x += 1
