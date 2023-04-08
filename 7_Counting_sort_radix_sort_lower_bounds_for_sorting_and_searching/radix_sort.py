#  radix sort has a time complexity of O(kn), where k is the maximum number of digits in any element of the list lst

def radix_sort(lst):
    # Find the maximum number to know the number of digits
    max_num = max(lst)
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(lst, exp)
        exp *= 10

def counting_sort(lst, exp):
    n = len(lst)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    # starting from the least significant digit and moving towards the most significant digit, using a base of 10.
    for i in range(n):
        index = lst[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = lst[i] // exp
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to lst[], so that lst[] now
    # contains sorted numbers according to current digit
    for i in range(n):
        lst[i] = output[i]
