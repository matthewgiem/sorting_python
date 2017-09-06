import math
from random import *
# open the doc
open_doc = open("array.txt")

# save the data
numbers_to_sort = open_doc.read()

# close the doc
open_doc.close()

answer = '2444678991011111112131616161717171819192023232426282929292929293133363838394040414142434546474747495151525357575859616262636363636464666667676868686870757777777879838788899191939495959699100100'

# print("the numbers to sort are")
# print(numbers_to_sort)
# numbers_unordered = []
# array = []
# array = numbers_to_sort.split()
# for x in array:
#     numbers_unordered.append(int(x))
# print(numbers_unordered)


# sorting algorythm
def bubble_sort(arg):
    sorted_numbers = arg
    array = []
    new_array = []
    array = sorted_numbers.split()
    for x in array:
        new_array.append(int(x))
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


    print("it took the bubble sort algorythm " + str(times) + " times to sort out of the max amout of times " + str(math.pow(len(new_array) - 1, 2)))
    print(times)
    print(new_array)
    print(''.join(map(str,new_array)) == answer)


def insersion_sort(arg):
    unsorted_numbers = arg
    array = []
    new_array = []
    array = unsorted_numbers.split()
    for x in array:
        new_array.append(int(x))
    # sort
    answer = '2444678991011111112131616161717171819192023232426282929292929293133363838394040414142434546474747495151525357575859616262636363636464666667676868686870757777777879838788899191939495959699100100'
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
    print("it took the insertion sort algorythm " + str(times) + " times to sort out of the max amout of times " + str(math.pow(len(new_array) - 1, 2)))
    print(times)
    print(new_array)
    print(''.join(map(str,new_array)) == answer)

def quick_sort(arg):
    unsorted_numbers = arg
    array = []
    new_array = []
    newer_array = []
    array = unsorted_numbers.split()
    for x in array:
        new_array.append(int(x))
    pick = new_array[randint(1, len(array))]
    print(new_array[pick])
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
    print(new_array[pick])
    print(less_than_array)
    less_than_array.append(new_array[pick])
    newer_array = less_than_array + greater_than_array
    print(newer_array)






quick_sort(numbers_to_sort)
# bubble_sort(numbers_to_sort)
# print("--------")
# insersion_sort(numbers_to_sort)
