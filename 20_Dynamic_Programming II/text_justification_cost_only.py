def compute_cost(words, i, j, L):
    # i번째 단어부터 j번째 단어까지의 길이를 구하고, 이를 구간의 길이로 저장합니다.
    length = sum([len(word) for word in words[i:j+1]]) + j - i

    # j가 리스트 words의 마지막 인덱스이고, 현재 구간의 길이가 L보다 작거나 같으면 0을 반환합니다.
    if j == len(words) - 1 and length <= L:
        return 0
    # 현재 구간의 길이가 L보다 크면 무한대 값을 반환합니다.
    elif length > L:
        return float('inf')
    else:
        # 현재 구간의 길이가 L보다 작으면, 비용을 계산하여 반환합니다.
        # 비용은 (L - length)의 세제곱으로 정의합니다.
        return (L - length) ** 2


def word_wrap(words, L):
    # 리스트 words의 길이를 n에 저장합니다.
    n = len(words)

    # n+1 크기의 리스트 dp를 생성합니다. dp[i]는 i번째 단어부터 마지막 단어까지
    # 한 줄로 출력할 때 필요한 최소 비용을 의미합니다.
    dp = [0] * (n + 1)

    # 리스트 words를 거꾸로 순회합니다. i는 현재 구간의 첫번째 단어를 의미합니다.
    for i in range(n-1, -1, -1):
        # i부터 j까지의 구간을 한 줄로 출력할 때 드는 비용을 계산하여
        # cost 리스트에 저장합니다. cost[j-i]는 i부터 j까지의 구간을 한 줄로
        # 출력할 때 드는 비용입니다.
        cost = [compute_cost(words, i, j, L) + dp[j+1] for j in range(i, n)]

        # cost 리스트 중 최소값을 dp[i]에 저장합니다.
        dp[i] = min(cost)

    # dp[0]은 첫번째 단어부터 마지막 단어까지 한 줄로 출력할 때 필요한 최소 비용입니다.
    return dp[0]


# Test case 1: Minimum possible cost with single word
assert word_wrap(["hello"], 5) == 0  # [0, 0]

# Test case 2: Minimum possible cost with multiple words
assert word_wrap(["hello", "world"], 20) == 0  # [0, 0, 0]

# Test case 3: Single line with word exceeding limit
assert word_wrap(["hello"], 3) == float('inf')  # [inf, 0]

# Test case 4: Single line with multiple words exceeding limit
assert word_wrap(["hello", "worlds"], 5) == float('inf')  # [inf, inf, 0]

# # Test case 5: Multiple lines with minimum cost
assert word_wrap(["This", "is", "a", "test"], 10) == 1  # [1, 0, 0, 0, 0]

# # Test case 6: Multiple lines with higher cost
assert word_wrap(["This", "is", "a", "test"], 5) == 2  # [2, 1, 64, 0, 0]

# # Test case 7: Multiple lines with higher cost and long words
assert word_wrap(["This", "is", "a", "verylongword", "test"],
                 10) == float('inf')  # [inf, inf, inf, inf, 0, 0]

