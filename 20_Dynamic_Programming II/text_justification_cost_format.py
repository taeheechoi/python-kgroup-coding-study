def compute_cost(words, i, j, L):
    length = sum([len(word) for word in words[i:j+1]]) + j - i
    if j == len(words) - 1 and length <= L:
        return 0
    elif length > L:
        return float('inf')
    else:
        return (L - length) ** 3


def word_wrap(words, L):
    n = len(words)
    dp = [0] * (n + 1)
    breaks = [0] * n  # list to store the index of the first word in each line

    for i in range(n-1, -1, -1):
        cost = [compute_cost(words, i, j, L) + dp[j+1] for j in range(i, n)]
        dp[i] = min(cost)
        
        breaks[i] = i + cost.index(dp[i])
    result = ''
    i = 0

    while i < n:
        j = breaks[i]
        result += ' '.join(words[i:j+1]) + '\n'
        i = j + 1
    print(dp, result)
    return dp[0], result

word_wrap(["hello"], 3)
word_wrap(["hello", "world"], 5) 

word_wrap(["This", "is", "a", "test"], 10)
word_wrap(["This", "is", "a", "test"], 5)
word_wrap(['Hello', 'world,', 'how', 'are', 'you', 'doing', 'today?'], 15)


# # Test case 3: Single line with word exceeding limit
# assert word_wrap(["hello"], 3) == float('inf') # [inf, 0]

# # Test case 4: Single line with multiple words exceeding limit
# assert word_wrap(["hello", "worlds"], 5) == float('inf') # [inf, inf, 0]

# # # Test case 5: Multiple lines with minimum cost
# assert word_wrap(["This", "is", "a", "test"], 10) == 1 # [1, 0, 0, 0, 0]

# # # Test case 6: Multiple lines with higher cost
# assert word_wrap(["This", "is", "a", "test"], 5) == 2 # [2, 1, 64, 0, 0]

# # # Test case 7: Multiple lines with higher cost and long words
# assert word_wrap(["This", "is", "a", "verylongword", "test"], 10) == float('inf') # [inf, inf, inf, inf, 0, 0]

