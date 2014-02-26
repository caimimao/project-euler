# -*- coding: utf-8 -*-

__title__ = "Primes with runs"

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

    d = range(0, 10) #0,1,...,9

    def m(n, d):
        if d == 0:
            # x00..0y, where x in (1,..,9) and y in (1,3,7,9)
            # x00..0y = y + x*10^n
            m, step = 0, 10**(n-1)
            found = False
            sum, count = 0, 0
            for x in range(1,10):
                m = m + step
                for y in [1,3,7,9]:
                    r = m + y
                    if is_a_prime(r):
                        found = True
                        sum += r
                        count += 1

            if found:
                return (n-2, count, sum)

        if d in range(1,10):
            # xddd = d*(1111) + (x-d)*10^3
            extra = 1
            for i in range(1, n):
                extra = extra*10 + 1
            extra = d*extra

            found = False
            sum, count = 0, 0
            for posx in range(0, n):
                for x in range(1, 10):
                    if x != d:
                        r = extra + (x-d)*10**posx
                        if is_a_prime(r):
                            found = True
                            sum += r
                            count += 1
            if found:
                return (n-1, count, sum)
            else:
                # dxdyd = 11111 + (x-d)*10^3 + (y-d)*10^2
                found = False
                sum, count = 0, 0
                for posx in range(0, n):
                    for posy in range(posx+1, n):
                        for x in range(0, 10):
                            for y in range(0, 10):
                                if posy == n-1 and y == 0:
                                    continue
                                if x != d and y != d:
                                    r = extra + (x-d)*10**posx + (y-d)*10**posy
                                    if is_a_prime(r):
                                        found = True
                                        sum += r
                                        count +=1

                if found:
                    return (n-2, count, sum)

    s = 0
    for d in xrange(0, 10):
        tmp = m(4, d)
        s = s + tmp[2]
        log("%d - %s" %(d, tmp))

    log("sum for 4:%d" % s)

    s = 0
    for d in xrange(0, 10):
        tmp = m(10, d)
        s = s + tmp[2]
        log("%d - %s" %(d, tmp))

    return s