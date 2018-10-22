# 1. If primes are divisable by only 1 and self, primes are not divisable by any other number
# 2. If any number is divisable by each of its divider's divider, primes are not divisable by any other prime
# 3. Following the sieve of erastothenes, primes are not divisable by any other prime smaller than their square root

from math import sqrt

pmax = 4194304                      # should take a couple of seconds


def erastothenes(m):
    """Returns the largest prime below m"""
    primes = []                     # Store primes in a sorted list
    for i in range(3, m, 2):        # Only check odd numbers
        prime = True                # Each iteration assumes a prime
        root = sqrt(i)              # Store sqrt of iterated number for speed (only calculate it once)
        for j in primes:            # Each jteration checks against all current primes
            if j > root: break      # But only ones defined in 3.
            elif i % j == 0:        # But only ones defined in 2.
                prime = False
                break               # Because primes[] are sorted, break ensures only necessary jterations
        if prime: primes.append(i)  # If jteration is prime, expand primes list without impacting checks for j
    return primes[-1]               # Remove slice to return list of found primes


print(erastothenes(pmax))
