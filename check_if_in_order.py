def check_if_in_order(arg):
    length = len(arg) - 1
    for x in range(length):
        if arg[x] > arg[x + 1]:
            return False
    return True
