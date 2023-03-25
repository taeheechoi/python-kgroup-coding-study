# The time complexity of Merge Sort is O(nlogn) in all 3 cases (worst, average, and best) 
# as merge sort always divides the array into two halves and takes linear time to merge two halves.
# The space complexity of Merge Sort is O(n) as all elements are copied into an auxiliary array. 
# So N auxiliary space is required for merge sort.

def merge_sort(arr):
    if len(arr) > 1:
        print(arr)
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        
        print('         location         |   i   |   j')
        i = j = k = 0
        while i < len(L) and j < len(R):
            print(f'i < len(L) and j < len(R) |   {i}   |   {j}   ')
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            print(f'i < len(L)                |   {i}   |')
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            print(f'j < len(R)                |       |   {j}   ')
            arr[k] = R[j]
            j += 1
            k += 1
    
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(arr))

# [12, 11, 13, 5, 6, 7]

# [12, 11, 13]
# [11, 13]
#          location         |   i   |   j
# i < len(L) and j < len(R) |   0   |   0   
# j < len(R)                |       |   0   
#          location         |   i   |   j
# i < len(L) and j < len(R) |   0   |   0   
# i < len(L) and j < len(R) |   0   |   1   
# j < len(R)                |       |   1   

# [5, 6, 7]
# [6, 7]
#          location         |   i   |   j
# i < len(L) and j < len(R) |   0   |   0   
# j < len(R)                |       |   0   
#          location         |   i   |   j
# i < len(L) and j < len(R) |   0   |   0   
# j < len(R)                |       |   0   
# j < len(R)                |       |   1   
#          location         |   i   |   j
# i < len(L) and j < len(R) |   0   |   0   
# i < len(L) and j < len(R) |   0   |   1   
# i < len(L) and j < len(R) |   0   |   2   
# i < len(L)                |   0   |
# i < len(L)                |   1   |
# i < len(L)                |   2   |
# [5, 6, 7, 11, 12, 13]