from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from optimized_bubble_sort import optimized_bubble_sort
from optimized_insertion_sort import optimized_insertion_sort
from quick_sort import quick_sort

# list_of_functions = [bubble_sort, optimized_bubble_sort, insertion_sort, optimized_insertion_sort, quick_sort]
list_of_functions = [optimized_insertion_sort, quick_sort]

def sort_report(arg):
    for lists in arg:
        for functions in list_of_functions:
            print("an array that has {} elements takes it {} times to sort using the {} algorythm".format(len(functions(lists)[0]), functions(lists)[1], functions(lists)[2]))
