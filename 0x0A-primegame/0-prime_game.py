#!/usr/bin/python3
"""
This module contains a function that returns the
the character with more wins and this is a mock
trial question
"""


def get_primes_up_to(n):
    """
    Return a list of prime numbers
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    primes = []

    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False

    return primes


def is_winner(rounds, nums):
    """
    Determines the winner
    """
    if rounds is None or nums is None or rounds == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(rounds):
        primes_count = len(get_primes_up_to(nums[i]))

        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
