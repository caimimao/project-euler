# -*- coding: utf-8 -*-

__title__ = "Totient maximum"

def solve():
    # Ref http://en.wikipedia.org/wiki/Totient_function
    # Phi(n) = n*Product[(1-1/p) for p|n]

    from common.util import get_prime_below_seive, isprime
    from math import sqrt
    from common import log

    limit = 1000000    
    seive = get_prime_below_seive(10000)
    primes = filter(None, seive)

    max = 1
    for i in primes:
        max = max*i
        if max > limit:
            return max/i



