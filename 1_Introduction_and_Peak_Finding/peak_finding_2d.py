# https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-1-algorithmic-thinking-peak-finding/
# The time complexity of the binary search algorithm used in the code is O(log n), where n is the number of rows in the 2D array. This is because the code performs a binary search on the rows of the array to find the peak element, and each row has a length of m, which is a constant.
# The space complexity of the binary search algorithm used in the code is O(1), which means that the amount of memory used by the code is constant and does not depend on the size of the input array. This is because the code only uses a few variables to keep track of the indices of the array, and does not create any additional data structures.

def find_peak_2d(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        max_col = arr[mid].index(max(arr[mid])) # index of max value in [14, 13, 12, 11] => 0 (14)  
        
        print(max_col)

        print(arr[mid - 1][max_col], arr[mid][max_col], arr[mid+1][max_col]) # first column 10 14 15

        if (mid == 0 or arr[mid - 1][max_col] <= arr[mid][max_col]) and (mid == right or arr[mid + 1][max_col] <= arr[mid][max_col]):
            return arr[mid][max_col]
        elif mid > 0 and arr[mid - 1][max_col] > arr[mid][max_col]:
            right = mid - 1
        else:
            left = mid + 1

    return None


test = [[10, 8, 10, 10],
        [14, 13, 12, 11],
        [15, 9, 11, 21],
        [16, 17, 19, 20]
        ]
print(find_peak_2d(test))
