# Programming Assignment #3
# Problem #3
# Counting Sort Algorithm


from random import randint
import time


def random_array():  # Creates and populates an array with random integers from 0 to 500, returning the array
    arr = []
    for i in range(5000):
        arr.append(randint(0, 500))
    return arr


def counting_sort(arr):  # Used counting sort algorithm create a new array where arr[i] is equal to the number of times
    # the number appears in the unsorted array. The index is value in this case.
    t_start = time.perf_counter()
    num = []
    for i in range(501):  # 501 is the size of the array due to the range being 0-500
        num.append(0)
    for i in range(len(arr)):  # Goes through the unsorted array and for each value increments the arr[i] in the new
        # array by 1
        num[arr[i]] = num[arr[i]] + 1
    t_end = time.perf_counter()
    print_100(num)
    print("\nTime elapsed:", t_end - t_start, "seconds.")


def print_array(num):  # Prints the entire array
    for i in range(len(num)):
        if num[i] > 0:
            for j in range(num[i]):
                print(i)


def print_100(arr):  # Prints out every 100th element in the array
    count = 0
    print("Printing every 100th element in the sorted array")
    for i in range(len(arr)):
        if arr[i] > 0:
            for j in range(arr[i]):
                count = count + 1
                if count % 100 == 0:
                    print(i, end=' ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = random_array()
    print("Counting Sort Alogorithm on a random array of integers from 0 - 500")
    counting_sort(arr)
    print("Press any key to close the program.")
    input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
