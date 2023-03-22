# https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-1-algorithmic-thinking-peak-finding/
# Time: O(log n)
# Space: O(1)
def find_peak_index(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == right or arr[mid + 1] <= arr[mid]):
            return mid
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None


test = [6, 7, 4, 3, 2, 1, 4, 5]
print(find_peak_index(test))
