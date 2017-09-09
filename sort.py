from insersion_sort import insersion_sort
from bubble_sort import bubble_sort
from print_answer import print_answer
from quick_sort import quick_sort
from check_if_in_order import check_if_in_order

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
# quick_sort(arg)
# print_answer(bubble_sort(arg))
# print_answer(insersion_sort(arg))
# correct = [1, 2, 3, 4, 5, 5]
# incorrect = [2, 4, 1]
# print(correct)
# print(check_if_in_order(correct))
# print("True")
# print("--------")
# print(incorrect)
# print(check_if_in_order(incorrect))
# print("False")
# print("--------")
# print(bubble_sort(arg)[0])
# print(check_if_in_order(bubble_sort(arg)[0]))
# print("True")
