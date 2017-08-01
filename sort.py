# open the doc
open_doc = open("array.txt")

# save the data
numbers_to_sort = open_doc.read()

# close the doc
open_doc.close()

# print the sorted numbers
print(numbers_to_sort)
