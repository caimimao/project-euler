# -*- coding: utf-8 -*-

__title__ = "Prime square remainders"

def solve():
    from common.util import get_prime_below_seive, isprime
    from math import sqrt
    from common import log

    limit = 250000
    limit_pow = limit*limit
    seive = get_prime_below_seive(limit)
    primes = filter(None, seive)

    def is_a_prime(n):
        if n >= limit:
            if n<limit_pow:
                from math import sqrt
                root = sqrt(n) + 1
                for p in primes:
                    if p > root:
                        break
                    if n % p == 0:
                        return False
                return True
            else:
                return isprime(n)
        else:
            return seive[n] != 0   

    n = 1
    for p in primes:
        if n % 2 == 0:
            r = 2
        else:
            r = 2*n*p
            log([p, n, r])
        if r>10**10:
            return n
        n = n + 1
