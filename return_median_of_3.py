import random
def return_median_of_3(array):
    length = len(array)
    partitions = []
    while len(partitions) < 3:
        to_append = random.randint(0, length - 1)
        if to_append in partitions:
            pass
        else:
            partitions.append(to_append)
    if partitions[0] < partitions[1]:
        if partitions[0] > partitions[2]:
            return partitions[0]
        else:
            if partitions[1] < partitions[2]:
                return partitions[1]
            else:
                return partitions[2]
    else:
        if partitions[0] < partitions[2]:
            return partitions[0]
        else:
            if partitions[1] < partitions[2]:
                return partitions[2]
            else:
                return partitions[1]
