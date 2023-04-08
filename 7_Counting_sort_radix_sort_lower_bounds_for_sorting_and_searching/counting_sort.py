def counting_sort(arr, max_val):
    n = len(arr)
    count_arr = [0] * (max_val + 1)
    output_arr = [0] * n

    # Count occurrences of each element
    for i in range(n):
        count_arr[arr[i]] += 1

    # Modify count_arr to get actual position of each element in output_arr
    for i in range(1, max_val + 1):
        count_arr[i] += count_arr[i - 1]

    # Build output_arr
    for i in range(n):
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1

    return output_arr
