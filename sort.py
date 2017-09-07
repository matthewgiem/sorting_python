from insersion_sort import insersion_sort
from bubble_sort import bubble_sort
from print_answer import print_answer
from quick_sort import quick_sort

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

# print_answer(bubble_sort(arg))
# print("--------")
# print_answer(insersion_sort(arg))
# print("--------")
# print_answer(quick_sort(arg))
quick_sort(arg)
