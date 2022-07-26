# Programming Assignment #3
# Question #4
# Radix Sort on an array with 5,000 integers ranging from 0 to 50,000

from random import randint
import time


# Populates an array of 5,000 elements with integers between 0 - 50,000
def populate_array():
    arr = []
    for i in range(5000):
        arr.append(randint(0, 50000))
    return arr


# Code to iterate through the significant digits and sorted it with radix sort based on that digit.
def radix(arr):
    exp = 1
    print("Starting Radix sort on Array of size", len(arr))
    t_start = time.perf_counter()
    while exp <= 10000:  # Statement determines the max significant digit to sort by.
        radix_sort(arr, exp)
        exp *= 10  # Iterates to the next significant digit
    t_end = time.perf_counter()
    print_first_last(arr)
    print("\nTime elapsed:", t_end - t_start, "seconds.\n")


def radix_sort(arr, exp):
    digit = [[] for _ in range(10)]
    for i in range(len(arr)):  # For loop that does modular division on the current significant figure, starting with
        index = (arr[i] // exp) % 10  # the 1's place, followed by 10's, 100's etc.
        digit[index].append(arr[i])  # The result is store in the variable index which is used to place the integer in
        # the correct bucket 0 - 9

    # Turns the 2D list of buckets into a 1D list that is sorted by the current significant digit.
    # This process is repeated until the max significant digit is reached, in this case 10000.
    count = 0
    for i in range(len(digit)):
        if len(digit[i]) != 0:
            for j in range(len(digit[i])):
                arr[count] = digit[i][j]
                count += 1


# Prints the first 100 elements and last 100 elements in ascending order
def print_first_last(arr):
    print("First 100 integers in ascending order.")
    for i in range(len(arr)):
        if i < 100 or len(arr) - 100 <= i < len(arr):
            if i % 10 == 0:
                print("")
            print(arr[i], end=' ')
        if i == 100:
            print("\n\nLast 100 integers in ascending order.")


if __name__ == '__main__':
    test = [11, 3002, 12, 384, 57, 93348, 57, 159]
    arr = populate_array()
    print("Radix sort on a test array for proof of concept")
    print("Test Array before Radix Sort")
    print(test)
    radix(test)
    print("Radix sort on 5,000 random integers between 0 - 50,000")
    radix(arr)
    print("Press any key to end the program")
    input()
