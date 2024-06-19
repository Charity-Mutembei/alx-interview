#!/usr/bin/python3
"""
Tak 0: Change comes from within
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    """
    Initialize dp array
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    """
    Fill dp array
    """
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
