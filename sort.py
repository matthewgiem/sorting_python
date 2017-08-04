import math
# open the doc
open_doc = open("array.txt")

# save the data
numbers_to_sort = open_doc.read()

# close the doc
open_doc.close()

# sorting algorythm
def bubble_sort(arg):
    sorted_numbers = arg
    array = []
    new_array = []
    array = sorted_numbers.split()
    for x in array:
        new_array.append(int(x))
    # sort
    answer = '2444678991011111112131616161717171819192023232426282929292929293133363838394040414142434546474747495151525357575859616262636363636464666667676868686870757777777879838788899191939495959699100100'
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

# bubble_sort(numbers_to_sort)

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
    x = 0
    j = 0
    times = 0
    for x in range(0, len(new_array) - 1):
        for i in range(0, len(new_array) - 1):
            if new_array[i] > new_array[i + 1]:
                num1 = new_array[i]
                num2 = new_array[i + 1]
                new_array[i] = num2
                new_array[i + 1] = num1
                if j in range(0, len(new_array) - x):
                    

            i += 1
            times += 1
            if i == len(new_array) - x:
                break
        x += 1

insersion_sort(numbers_to_sort)
