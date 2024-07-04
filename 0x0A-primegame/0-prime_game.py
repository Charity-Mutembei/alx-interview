#!/usr/bin/python3
"""
Function returning winner in a prime game
"""


def set_primes(k):
    """Function returning a list of primes up to k"""
    prime = []
    sieve = [True] * (k + 1)
    for p in range(2, k + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, k + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """Function returning winner in a prime game"""
    if x is None or x == 0 or nums is None or nums == []:
        return None
    Maria = 0
    Ben = 0

    for i in range(x):
        prime_number = set_primes(nums[i])

        if len(prime_number) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Ben > Maria:
        return "Ben"
    elif Maria > Ben:
        return "Maria"
    return None
