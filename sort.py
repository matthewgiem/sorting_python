# open the doc
open_doc = open("array.txt")

# save the data
numbers_to_sort = open_doc.read()

# close the doc
open_doc.close()

# sorting algorythm
def sort(arg):
    sorted_numbers = arg
    print(sorted_numbers)

sort(numbers_to_sort)
