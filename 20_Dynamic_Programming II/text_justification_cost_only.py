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
   
    return dp[0], result


# def compute_cost(words, i, j, L):
#     """
#     Computes the cost of arranging the words from i to j in a single line with a width limit of L.
#     """
#     length = sum([len(word) for word in words[i:j+1]]) + j - i

#     if j == len(words) - 1 and length <= L:
#         return 0
#     elif length > L:
#         return float('inf')
#     else:
#         return (L - length) ** 3


# def word_wrap(words, L):
#     """
#     Returns the minimum cost of arranging the words with a width limit of L.
#     """
#     n = len(words)

#     dp = [0] * (n + 1)
#     for i in range(n-1, -1, -1):
#         cost = [compute_cost(words, i, j, L) + dp[j+1] for j in range(i, n)]
#         dp[i] = min(cost)
#     print(dp)
#     return dp[0]

# Test 1
# words = ['Hello', 'world,', 'how', 'are', 'you', 'doing', 'today?']
# L = 15
# print(word_wrap(words, L))

# # # Test 2
# words = ['This', 'is', 'a', 'test']
# L = 7
# word_wrap(words, L)

# # # Test 3
# words = ['a', 'b', 'c', 'd', 'e']
# L = 3
# word_wrap(words, L)

# # # Test 4
# words = ['aaa', 'bb', 'c', 'd', 'ee', 'ff', 'ggg']
# L = 6
# word_wrap(words, L)

# # # Test 5
# words = ['a', 'b', 'c', 'd', 'e']
# L = 1
# word_wrap(words, L) 

# Test case 1: Minimum possible cost with single word
# assert word_wrap(["hello"], 5) == 0

# # Test case 2: Minimum possible cost with multiple words
# assert word_wrap(["hello", "world"], 20) == 0

# Test case 3: Single line with word exceeding limit
assert word_wrap(["hello"], 3) == float('inf') # [inf, 0]

# Test case 4: Single line with multiple words exceeding limit
assert word_wrap(["hello", "worlds"], 5) == float('inf') # [inf, inf, 0]

# # Test case 5: Multiple lines with minimum cost
assert word_wrap(["This", "is", "a", "test"], 10) == 1 # [1, 0, 0, 0, 0]

# # Test case 6: Multiple lines with higher cost
assert word_wrap(["This", "is", "a", "test"], 5) == 2 # [2, 1, 64, 0, 0]

# # Test case 7: Multiple lines with higher cost and long words
assert word_wrap(["This", "is", "a", "verylongword", "test"], 10) == float('inf') # [inf, inf, inf, inf, 0, 0]

# 위의 코드에서 compute_cost 함수는 i번째 단어부터 j번째 단어까지 한 줄에 나열했을 때, 해당 줄에 들어갈 문자열의 비용을 계산하는 함수입니다.
# 이때, 비용은 다음과 같이 계산됩니다.
# i번째 단어부터 j번째 단어까지 한 줄에 나열했을 때, 해당 줄에 들어갈 문자열의 길이 L를 계산합니다
# i번째 단어부터 j번째 단어까지 한 줄에 나열했을 때, 해당 줄에 들어갈 문자열의 비용 C를 계산합니다.
# - C = (L - len(단어들)) ^ 3, if j != n and L >= len(단어들)
# - C = 0, if j == n and L >= len(단어들)
# - C = float('inf'), otherwise (j != n and L < len(단어들))

# 이 함수를 이용하여 부분 문제의 최적 해결 방법을 찾고, 전체 문제의 최적 해결 방법을 구하는 과정을 구현합니다. 마지막으로, 최소 비용을 출력합니다.

# 위 코드에서는 dp 배열을 이용하여 다이나믹 프로그래밍을 수행합니다. dp[i]는 i번째 단어부터 n번째 단어까지 한 줄로 나열했을 때, 최소 비용을 의미합니다.

# 이때, 다음과 같은 점화식을 이용하여 부분 문제의 해결 방법을 구합니다.

# dp[i] = min(dp[j+1] + C(i, j)) for i <= j < n
# 위 점화식에서 dp[j+1]은 j+1번째 단어부터 n번째 단어까지 한 줄로 나열했을 때의 최소 비용을 의미합니다. C(i, j)는 i번째 단어부터 j번째 단어까지 한 줄에 나열했을 때의 비용을 계산하는 함수입니다.

# 이 점화식을 이용하여 dp 배열을 구하면, dp[0]에는 전체 문제의 최적 해결 방법인 최소 비용이 저장됩니다.

# 따라서, 위 코드를 실행하면 입력받은 문자열을 글정렬한 결과의 최소 비용이 출력됩니다.
