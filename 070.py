# -*- coding: utf-8 -*-

__title__ = "Totient permutation"

def solve():

    # Ref http://www.mathblog.dk/project-euler-70-investigate-values-of-n-for-which-%CF%86n-is-a-permutation-of-n/
    from common.util import get_prime_below_seive, isprime
    from math import sqrt
    from common import log

    limit = 5000
    limit_pow = limit*limit
    seive = get_prime_below_seive(limit)
    primes = filter(None, seive)

    ## Phi(n) = n*Product[(1-1/p) for p|n]
    def match(n, m):
        n = list(str(n))
        m = list(str(m))
        if len(m) != len(n):
            return False

        n.sort()
        m.sort()
        if m != n:
            return False
        return True

    max = 10000000000000
    result = None
    for x in xrange(0, len(primes)):
        for y in xrange(x+1, len(primes)):
            i = primes[x]*primes[y]
            if i > 10**7:
                break
            p = (primes[x]-1)*(primes[y]-1)
            if match(p, i):
                if i*1.0/p < max:
                    log([i, p, i*1.0/p])
                    max = i*1.0/p
                    result = i
    return result
