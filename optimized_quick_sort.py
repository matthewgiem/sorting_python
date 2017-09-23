import random
from optimized_insertion_sort import optimized_insertion_sort
def optimized_quick_sort(arg):
    array = list(arg[0])
    type_of_data = arg[1]
    times = 0
    swaps = 0

    j = 0
    for i in range(len(array)):
        print(array)
        print("j = {}".format(j))
        print("i = {}".format(i))
        print("comparing {} and {}".format(array[i], array[-1]))
        if array[i] <= array[-1]:
            print("{} <= {} so we are swapping {} with {}".format(array[i], array[-1], array[i], array[j]))
            # print("the elemet being compared to {} is {}".format(array[-1], array[i]))
            array[i], array[j] = array[j], array[i]
            j +=1
        print(array)



    return array, times, "Quick Sort", swaps, arg[0], type_of_data

def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
	if hi-low < threshold and low < hi:
		quick_selection(A, low, hi)
	elif low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)

def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi

def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)

def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]
