#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n,
write a method that calculates the fewest number of
operations needed to result in exactly n H characters
in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    write a method that calculates the fewest number of
    operations needed to result in exactly n H characters
    in the file.
    """
    if n <= 1:
        return 0

    """
    Initialize an array to store the minimum operations
    needed for each position
    """
    dp = [float('inf')] * (n + 1)

    """
    Base case: 0 operations needed for position 1
    """
    dp[1] = 0

    for i in range(2, n + 1):

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)

        if dp[i] == float('inf'):
            dp[i] = i

    return dp[n]
