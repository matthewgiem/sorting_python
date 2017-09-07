# from random import *
def quick_sort(arg):
    new_array = arg
    x = 0
    j = 0
    i = -1
    for x in range(0, len(new_array) - 1):
        if new_array[i] < new_array[x]:
            num1 = new_array[i]
            num2 = new_array[x]
            new_array[i] = num2
