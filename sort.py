from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from print_answer import print_answer
from quick_sort import quick_sort
from check_if_in_order import check_if_in_order
from optimized_bubble_sort import optimized_bubble_sort
from optimized_insertion_sort import optimized_insertion_sort

# open the doc
open_doc = open("array.txt")

# save the data
numbers_to_sort = open_doc.read()

# close the doc
open_doc.close()

# turn array of strings to array of integers
array = numbers_to_sort.split()
arg = []
for x in array:
    arg.append(int(x))

test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
almost = [1, 2, 3, 4, 3, 6, 9, 10, 8, 9]
# finished
# ----------------------- #
# print_answer(bubble_sort(arg))
# print_answer(optimized_bubble_sort(arg))
# print_answer(insertion_sort(arg))
# print_answer(bubble_sort(test))
# print_answer(insertion_sort(test))
# print_answer(optimized_bubble_sort(test))
# print_answer(bubble_sort(almost))
# print_answer(optimized_bubble_sort(almost))
# print_answer(insertion_sort(almost))

# working on
# ---------------------- #
print_answer(optimized_insertion_sort(arg))
