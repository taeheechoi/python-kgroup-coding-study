# The average case time complexity of insertion sort is O(N^2). 
# The time complexity of the best case is O(N). The space complexity is O(1).

def insert_sort(arr):
    # print('loc|   i   |   j   |   arr')
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            # print(f'in |   {i}   |   {j}   | {arr}')
            
            j -= 1

        arr[j + 1] = key
        # print(f'out|   {i}   |   {j}   | {arr}')
    return arr

arr = [5, 2, 4, 6, 1, 3]
print(insert_sort(arr))

# loc|   i   |   j   |   arr
# in |   1   |   0   | [5, 5, 4, 6, 1, 3]
# out|   1   |  -1   | [2, 5, 4, 6, 1, 3]

# in |   2   |   1   | [2, 5, 5, 6, 1, 3]
# out|   2   |   0   | [2, 4, 5, 6, 1, 3]

# out|   3   |   2   | [2, 4, 5, 6, 1, 3]

# in |   4   |   3   | [2, 4, 5, 6, 6, 3]
# in |   4   |   2   | [2, 4, 5, 5, 6, 3]
# in |   4   |   1   | [2, 4, 4, 5, 6, 3]
# in |   4   |   0   | [2, 2, 4, 5, 6, 3]
# out|   4   |  -1   | [1, 2, 4, 5, 6, 3]

# in |   5   |   4   | [1, 2, 4, 5, 6, 6]
# in |   5   |   3   | [1, 2, 4, 5, 5, 6]
# in |   5   |   2   | [1, 2, 4, 4, 5, 6]
# out|   5   |   1   | [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]