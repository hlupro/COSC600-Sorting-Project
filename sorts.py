# Programming Assignment #3
# Question 2
# Insertion, Selection, Bubble, and Merge Sort Algorithms

from random import randint
import time


def random_array():  # Creates and populates an array with random integers from 0 to 50000, returning the array
    arr = []
    for i in range(5000):
        arr.append(randint(0, 50000))
    return arr


def test_array():
    arr = [10, 2, 1, 7, 0, 39, 41, 12]
    return arr


def insert_sort(arr):
    t_start = time.perf_counter()
    index = 1  # Value to be compared against already sorted section of array, starts at index 1 and up to N
    while index < len(arr):  # Loop increments the index value which is compared to the sorted portion
        for i in range(index):  # Loops through the sorted portion of the array to insert the index value.
            if arr[index] < arr[i]:
                temp = arr[i]
                arr[i] = arr[index]
                arr[index] = temp
        index = index + 1
    t_end = time.perf_counter()
    print_array(arr)
    print("\nTime elapsed:", t_end - t_start, "seconds.\n")


# Iterates through the array and starts by sorted elements from 0 to i
def selection_sort(arr):
    t_start = time.perf_counter()
    for i in range(len(arr)):
        min = 999999
        mindex = 0
        j = i
        while j < len(arr):
            if arr[j] < min:
                mindex = j
                min = arr[j]
            j = j + 1
        temp = arr[i]
        arr[i] = arr[mindex]
        arr[mindex] = temp
    t_end = time.perf_counter()
    print_array(arr)
    print("\nTime elapsed:", t_end - t_start, "seconds.\n")


def bubble_sort(arr):
    t_start = time.perf_counter()
    swap = 1
    while swap == 1:
        swap = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = 1
    t_end = time.perf_counter()
    print_array(arr)
    print("\nTime elapsed:", t_end - t_start, "seconds.\n")


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]  # using python slicers to split the array

        right = arr[mid:]

        merge_sort(left)  # Merge sort on both sides

        merge_sort(right)

        i = j = k = 0

        # Compares the two sides and merges them up into a newly sorted one.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Catch any leftover elements in either the left or right side arrays and adds them to the sorted array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def print_array(arr):
    print("Printing the first 100 integers in the sorted array.")
    for i in range(len(arr)):
        if i < 100:
            print(arr[i], end=' ')
        if i == 32 or i == 65:
            print("")
    print("")


def merge(arr):
    t_start = time.perf_counter()
    merge_sort(arr)
    t_end = time.perf_counter()
    print_array(arr)
    print("\nTime elapsed:", t_end - t_start, "seconds.\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = random_array()
    arr1 = random_array()
    arr2 = random_array()
    arr3 = random_array()
    print("Insertion Sort")
    insert_sort(arr)
    print("Selection Sort")
    selection_sort(arr1)
    print("Bubble Sort")
    bubble_sort(arr2)
    print("Merge Sort")
    merge(arr3)
    print("Press any key to close the program.")
    input()

