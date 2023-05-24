def alternating_coin_game(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]

    for gap in range(n):
        for i in range(n - gap):
            j = i + gap
            if i == j:
                dp[i][j] = coins[i]
            else:
                dp[i][j] = max(coins[i] - dp[i + 1][j], coins[j] - dp[i][j - 1])

    return dp[0][n - 1]


# Example usage:
coins = [8, 15, 3, 7]
game_result = alternating_coin_game(coins)
print("Maximum total value of coins collected:", game_result)