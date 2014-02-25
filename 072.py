# -*- coding: utf-8 -*-

__title__ = "Counting fractions"

def solve():
    from math import sqrt

    limit = 10**6
    phi = [x for x in xrange(0, limit+1)]
    phi[0] = 0
    phi[1] = 0

    for n in xrange(2, limit+1):
        if phi[n] == n:
            for m in xrange(n, limit+1, n):
                phi[m] = phi[m]*(n-1)/n

    return sum(phi)

def solve1():
    from common.util import get_prime_below_seive, isprime
    from math import sqrt
    from common import log

    limit = 5000
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

    ## Phi(n) = n*Product[(1-1/p) for p|n]
    def phi(n):
        origin = n
        s = n
        for p in primes:
            if n % p == 0:
                s = s*(p-1)/p
                n = n // p
                while n % p == 0:
                    n = n // p
        if n > 1:
            s = s*(n-1)/n
        return s

    s = 0
    for i in xrange(2, 10**6+1):
        s = s + phi(i)

    return s

