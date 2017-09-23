from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from print_answer import print_answer
from quick_sort import quick_sort
from check_if_in_order import check_if_in_order
from optimized_bubble_sort import optimized_bubble_sort
from optimized_insertion_sort import optimized_insertion_sort
from return_median_of_3 import return_median_of_3
from sort_report import sort_report
from list_maker import list_maker
from optimized_quick_sort import optimized_quick_sort
import random



# open the doc
open_doc = open("array.txt")

# save the data
numbers_to_sort = open_doc.read()

# close the doc
open_doc.close()

# turn array of strings to array of integers
array = numbers_to_sort.split()
random_numbers = []
for x in array:
    random_numbers.append(int(x))
arg = [random_numbers, "large group of random numbers"]
test = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "reversed"]
almost = [[10, 2, 3, 1, 4, 3, 5, 10, 8, 9], "few swaps"]
random_ten = [[2,5,1,7,9,3,10,4,6,8], "random 10"]
# print(return_median_of_3(test[0]))
# finished
# ----------------------- #
# print_answer(bubble_sort(arg))
# print_answer(optimized_bubble_sort(arg))
# print_answer(insertion_sort(arg))
# print_answer(optimized_insertion_sort(arg))
# print_answer(quick_sort(arg))
# print_answer(bubble_sort(test))
# print_answer(insertion_sort(test))
# print_answer(optimized_bubble_sort(test))
# print_answer(optimized_insertion_sort(test))
# print_answer(quick_sort(test))
# print_answer(bubble_sort(almost))
# print_answer(optimized_bubble_sort(almost))
# print_answer(insertion_sort(almost))
# print_answer(optimized_insertion_sort(almost))
# print_answer(quick_sort(almost))

# sort_report([arg, test, almost])
# sort_report(list_maker(2, 500, 1000, 9))


# working on
# ---------------------- #

print_answer(optimized_quick_sort(random_ten))
