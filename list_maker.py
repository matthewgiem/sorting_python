import random
def list_maker(how_many_lists, minimum_list_length, maximum_list_length, largest_number_in_list):
    lists_of_lists_for_tests = []
    for x in range(how_many_lists):
        array = []
        for y in range(random.randint(minimum_list_length, maximum_list_length)):
            array.append(random.randint(0, largest_number_in_list))
        arrays = [array, "This array has {} elements is random".format(len(array))]
        lists_of_lists_for_tests.append(arrays)
    return lists_of_lists_for_tests
