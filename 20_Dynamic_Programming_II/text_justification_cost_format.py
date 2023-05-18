def compute_cost(words, i, j, L):
    """
    i번째 단어부터 j번째 단어까지 한 줄에 나열했을 때, 해당 줄에 들어갈 문자열의 비용을 계산합니다.
    """
    length = sum([len(word) for word in words[i:j+1]]) + j - i
    if j == len(words) - 1 and length <= L:
        return 0
    elif length > L:
        return float('inf')
    else:
        return (L - length) ** 2


def word_wrap(words, L):
    n = len(words)
    dp = [0] * (n + 1) # [66, 42, 57, 77, 41, 37, 1, 0, 0, 0]
    breaks = [0] * n  # list to store the index of the first word in each line [1, 3, 3, 3, 4, 5, 7, 8, 8]

    for i in range(n-1, -1, -1):
        cost = [compute_cost(words, i, j, L) + dp[j+1] for j in range(i, n)] # [78, 66, 78, inf, inf, inf, inf, inf, inf]
        dp[i] = min(cost)

        breaks[i] = i + cost.index(dp[i])
    result = ''
    i = 0

    while i < n:
        j = breaks[i]
        result += ' '.join(words[i:j+1]) + '\n'
        i = j + 1

    return dp[0], result


# assert word_wrap(["test"], 10) == (0, "test\n")
# assert word_wrap(["test", "is", "good"], 6) == (18, "test\nis\n")
# assert word_wrap(["test", "is"], 5) == (1, "test\nis\n")
assert word_wrap(["This", "is", "a", "long", "sentence", "that", "should", "be", "wrapped"], 10) == (
    66, 'This is\na long\nsentence\nthat\nshould be\nwrapped\n')

# 1st
# n 9
# i 8
# j 8 
# L 10
# length 7
# words wrapped
# breaks [0, 0, 0, 0, 0, 0, 0, 0, 8]
# cost [0]
# dp [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 2nd 
# n 9
# i 7
# j 7 
# L 10
# length 6
# words be wrapped
# breaks [0, 0, 0, 0, 0, 0, 0, 8, 8]
# cost [64, 0]
# dp [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ....

# Last
# n 9
# i 9
# j 8 
# L 10
# length 6
# words ['This', 'is', 'a', 'long', 'sentence', 'that', 'should', 'be', 'wrapped']
# breaks [1, 3, 3, 3, 4, 5, 7, 8, 8]
# cost [78, 66, 78, inf, inf, inf, inf, inf, inf]
# dp [66, 42, 57, 77, 41, 37, 1, 0, 0, 0]
# result 'This is\na long\nsentence\nthat\nshould be\nwrapped\n'