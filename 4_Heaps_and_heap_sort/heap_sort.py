# Heap Sort has a time complexity of O(n log n). 
# The efficiency of Heap Sort depends on the time required to build the max-heap, which has a time complexity of O(n), 
#and the time required to perform the swap and reconstruct the max-heap, which has a time complexity of O(log n). 
#Therefore, the overall time complexity of Heap Sort is O(n log n).
# Heap Sort is an in-place sorting algorithm requiring O(1) space complexity.

def max_heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]

max_heapify(arr, len(arr), 0)
print(arr)

heapSort(arr)
print(arr)
