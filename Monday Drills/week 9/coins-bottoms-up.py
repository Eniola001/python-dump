# Problem
# Write two functions that use a table (a list), not recursion:
# count_ways_dp(amount, coins): the number of combinations of coins that make amount (order does not matter, coins can be reused). This is last week’s count_ways, rewritten.
# min_coins(amount, coins): the fewest coins needed to make amount, or -1 if it is impossible.

# Examples
# count_ways_dp(5, [1, 2, 5])             # 4
# count_ways_dp(100, [1, 5, 10, 25, 50])  # 292
# count_ways_dp(0, [1, 2])                # 1
# min_coins(11, [1, 2, 5])                # 3   (5 + 5 + 1)
# min_coins(100, [1, 5, 10, 25, 50])      # 2   (50 + 50)
# min_coins(3, [2])                       # -1
# min_coins(0, [1])                       # 0

# Constraints
# Both functions use a list of size amount + 1 and loops. No recursion.
# Do not modify the coins list.
# Handle: empty coins, amount 0, and coins larger than the amount.
# Run count_ways_dp(10000, [1, 5, 10, 25, 50]). It must finish quickly. In a comment, explain why last week’s recursive version could not.

# Hint
# For min_coins, ask: “What is the best way to make a, if my last coin was c?”

# BonusHandle: empty coins, amount 0, and coins larger than the amount.
# Make min_coins also return which coins were used, for example (3, [5, 5, 1]).

# What this gauges: Can you turn a recursive idea into a table that fills from the bottom up? Can you explain why it is faster and why it never hits the recursion limit?

def count_ways_dp(amount, coins):
    # dp[a] represents the number of ways to make amount a.
    dp = [0] * (amount + 1)

    # There is exactly one way to make 0: use no coins.
    dp[0] = 1

    # Process each coin to avoid counting different orders separately.
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


def min_coins(amount, coins):
    # dp[a] represents the minimum coins needed to make amount a.
    dp = [float('inf')] * (amount + 1)

    # Track which coin was used to reach each amount.
    previous_coin = [None] * (amount + 1)

    # Zero coins are needed to make amount 0.
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                previous_coin[a] = coin

    # If the amount is impossible, return -1.
    if dp[amount] == float('inf'):
        return -1, []

    # Reconstruct the coins used.
    used_coins = []
    current = amount

    while current > 0:
        coin = previous_coin[current]
        used_coins.append(coin)
        current -= coin

    return dp[amount], used_coins


# The recursive version could not efficiently handle large amounts
# because it repeatedly recalculated the same subproblems and created
# many function calls, eventually risking Python's recursion limit.
# Dynamic programming stores results in a table and reuses them.

# Examples
print(count_ways_dp(5, [1, 2, 5]))             # 4
print(count_ways_dp(100, [1, 5, 10, 25, 50]))  # 292
print(count_ways_dp(0, [1, 2]))                # 1
print(count_ways_dp(10000, [1, 5, 10, 25, 50])) 

print(min_coins(11, [1, 2, 5]))                # (3, [5, 5, 1])
print(min_coins(100, [1, 5, 10, 25, 50]))      # (2, [50, 50])
print(min_coins(3, [2]))                       # (-1, [])
print(min_coins(0, [1]))                       # (0, [])
print(min_coins(7, []))                        # (-1, [])