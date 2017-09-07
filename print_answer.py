import math
answer = '2444678991011111112131616161717171819192023232426282929292929293133363838394040414142434546474747495151525357575859616262636363636464666667676868686870757777777879838788899191939495959699100100'
def print_answer(arg):
    array = arg[0]
    times = arg[1]
    print("it took the bubble sort algorythm " + str(times) + " times to sort out of the max amout of times " + str(math.pow(len(array) - 1, 2)))
    print(times)
    print(array)
    print(''.join(map(str,array)) == answer)
