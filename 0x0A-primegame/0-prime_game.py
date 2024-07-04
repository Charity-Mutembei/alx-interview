#!/usr/bin/python3
"""
This module contains a function that returns the
the character with more wins and this is a mock
trial question
"""


def isWinner(x, nums):
    max_n = max(nums)

    def sieve_of_eratosthenes(limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while (p * p <= limit):
            if sieve[p]:
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
            p += 1
        return [p for p in range(limit + 1) if sieve[p]]

    primes = sieve_of_eratosthenes(max_n)

    def winner_for_round(n):
        if n == 1:
            return 'Ben'

        count = 0
        for prime in primes:
            if prime > n:
                break
            count += 1

        if count % 2 == 1:
            return 'Maria'
        else:
            return 'Ben'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = winner_for_round(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
