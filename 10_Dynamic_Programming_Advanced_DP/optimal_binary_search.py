def binary_search(arr, low, high, target, memo):
    if high >= low:
        mid = low + (high - low) // 2

        # Check if the subproblem result is already computed
        if memo[low][high] != -1:
            return memo[low][high]

        # If the target is found at the middle element
        if arr[mid] == target:
            memo[low][high] = mid
            return mid

        # If the target is smaller than the middle element, search the left subarray
        elif arr[mid] > target:
            memo[low][high] = binary_search(arr, low, mid - 1, target, memo)
            return memo[low][high]

        # If the target is greater than the middle element, search the right subarray
        else:
            memo[low][high] = binary_search(arr, mid + 1, high, target, memo)
            return memo[low][high]

    # If the target is not present in the array
    else:
        return -1

def optimal_binary_search(arr, target):
    n = len(arr)
    memo = [[-1] * n for _ in range(n)]
    return binary_search(arr, 0, n - 1, target, memo)


arr = [2, 4, 6, 8, 10]
target = 6

# Perform optimal binary search on the array
result = optimal_binary_search(arr, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in the array")