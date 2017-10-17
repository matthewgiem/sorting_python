from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from optimized_bubble_sort import optimized_bubble_sort
from optimized_insertion_sort import optimized_insertion_sort
from optimized_quick_sort import optimized_quick_sort
from new_quick_sort import new_quick_sort
from new_quick_sort import bubble_sort_for_quick_sort
import random

def list_of_algorythms():
    print('''
    1.  Bubble Sort
    2.  Insertion Sort
    3.  Quick Sort
    4.  Optimized version of Bubble Sort
    5.  Optimized version of Insertion Sort
    ''')

def what_type_of_data():
    while True:
        number_of_integers = raw_input("how many data points would you like > ")
        if number_of_integers.lower() == "stop":
            break
        elif int(number_of_integers) < 10:
            print("you need to choose a value greater than or equal to 10")
        else:
            return number_of_integers

while True:
    print("Welcom to my sorting program")
    print("The use of this is to demonstrat my profeciency using sorting algorythms")
    print("If at any time you wish to exit the program just enter 'STOP' in to the prompt")
    list_of_algorythms()
    choice = raw_input("what algorythm do you wanna use? ")
    if choice == "STOP":
        print("thanks for using the sorting service")
        break
    what_type_of_data()
    print("end of program")
