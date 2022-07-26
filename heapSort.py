# Programming Assignment #3
# Question 1
# Heap Sort algorithms

from random import randint
import time

# Global variable for swap
swap = 0


def random_array():  # Creates and populates an array with random integers from 0 to 500, returning the array
    arr = []
    for i in range(5000):
        arr.append(randint(0, 50000))
    return arr


# Insert function for the heap that inserts a function at the end of the heap and then if it's invalid, pushes up
# through the parents to its right spot
def heap_insert(heap, x):
    heap.append(x)
    iter = len(heap) - 1
    if len(heap) > 1:
        while heap[iter] < heap[(iter - 1) // 2] and iter > 0:
            temp = heap[(iter - 1) // 2]
            heap[(iter - 1) // 2] = heap[iter]
            heap[iter] = temp
            iter = (iter - 1) // 2
            global swap
            swap += 1


# Main function used to keep the heap valid, acts recursively up the heap through the parent until valid
def heapify(heap, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(heap) and heap[smallest] > heap[left]:
        smallest = left
    if right < len(heap) and heap[smallest] > heap[right]:
        smallest = right
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        global swap
        swap += 1
        heapify(heap, smallest)


# Delete Min is used to print out the sorted array by popping the min and then adjusting the heap
def delete_min(heap, count):
    heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
    min = heap.pop(len(heap) - 1)
    if count < 50:
        print(min, end=' ')
    if count == 24:
        print("")
    heapify(heap, 0)


# Heap sort where the heap is created by inserting random integers  0 - 50,000 in an empty heap
def heap_sort(arr):
    t_start = time.perf_counter()
    heap = []
    count = 0
    for i in range(len(arr)):  # Inserting the elements into the Heap here
        heap_insert(heap, arr[i])
    print("Printing out the first 50 elements")
    while len(heap) > 1:
        delete_min(heap, count)
        count += 1
    t_end = time.perf_counter()
    print("\n\nTime elapsed:", t_end - t_start, "seconds.")
    print("Total Swaps: ", swap)
    print("")


# Heap sort done with linear build heap algorithm, integers are pushed into an array which is than heapified
def linear_heap_sort(arr):
    # heap = arr
    count = 0
    i = ((len(arr) - 1) - 1) // 2
    t_start = time.perf_counter()
    while i >= 0:
        heapify(arr, i)
        i -= 1
    print("Printing out first 50 elements\n")
    while len(arr) > 1:
        delete_min(arr, count)
        count += 1
    t_end = time.perf_counter()
    print("\n\nTime elapsed:", t_end - t_start, "seconds.")
    print("Total Swaps: ", swap)
    print("")


if __name__ == '__main__':
    arr1 = random_array()
    arr2 = random_array()
    print("HeapSort on a heap that was built with the insert function")
    heap_sort(arr2)
    if swap != 0:
        swap = 0
    print("HeapSort on Linear Build Heap Algorithm")
    linear_heap_sort(arr1)
    print("Press any key to close the program.")
    input()
