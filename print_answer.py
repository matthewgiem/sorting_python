import math
from check_if_in_order import check_if_in_order
def print_answer(arg):
    sorted_array = arg[0]
    times = arg[1]
    name = arg[2]
    swaps = arg[3]
    original = arg[4]
    type_of_data = arg[5]
    if check_if_in_order(sorted_array) == False:
        print("False")
        print("the original array was \n{}".format(original))
        print("it got converted to \n{}".format(sorted_array))
    else:
        print("it took the {} algorythm {} times to sort {} out of the max amout of times {} utilizing {} number of swaps".format(name, times, type_of_data, math.pow(len(sorted_array) - 1, 2), swaps))
        if len(original) < 11:
            print(original)
            print(sorted_array)
        else:
            print("\n")
