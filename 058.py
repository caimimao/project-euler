# -*- coding: utf-8 -*-

__title__ = "Spiral primes"

def solve():
    from common.util import get_prime_below_seive, isprime
    from math import sqrt
    from common import log

    limit = 200000
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

    total = 1
    count = 0
    sa = 1
    level = 2
    while True:
        sa = sa + 8*(level-2) + 2
        gap = 2*(level-1)
        numbers = [sa, sa+gap, sa+2*gap] #ignore sa+3*gap (=[2*level + 1]^2)
        for p in numbers:
            if is_a_prime(p):
                count = count + 1
        total = total + 4

        if (count*10 < total) :
            log("level=%d" % level)
            log("%d/%d" % (count, total))
            return 2*(level-1) + 1

        level = level + 1

