#!/usr/bin/python3
"""
Tak 0: Change comes from within
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
            # Early exit if we find the exact match
            if dp[total] != float('inf'):
                return dp[total]

    return dp[total] if dp[total] != float('inf') else -1
