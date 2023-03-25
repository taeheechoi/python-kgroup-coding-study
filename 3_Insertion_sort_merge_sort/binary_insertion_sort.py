# better than insert_sort
# comparison: NlogN, swap: n^2
# The time complexity of binary insertion sort in the average and worst case is O(N^2). 
# While for the best case, the time complexity will be O(NlogN). 
# It is because the number of comparisons for inserting one element is O(log N), and for N elements, it will be O(NlogN).
# The space complexity of binary insertion sort is O(1).

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, key, 0, i - 1)
        for j in range(i - 1, pos - 1, -1):
            arr[j + 1] = arr[j]
        arr[pos] = key
    return arr

def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1)
    else:
        return mid

arr = [5, 2, 4, 6, 1, 3]
print(binary_insertion_sort(arr))