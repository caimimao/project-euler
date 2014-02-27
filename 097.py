# -*- coding: utf-8 -*-

__title__ = "Large non-Mersenne prime"

def solve():
    # 28433*2^7830457+1
    from common import log

    limit = 10**10

    pow_of_twos = {}
    pow_of_twos[1] = 2
    for i in range(0,22):
        j = 2**i
        a = pow_of_twos[j]
        b = a*a % limit
        pow_of_twos[2*j] = b

    pows = sorted(pow_of_twos.keys())
    pows.reverse()

    powers = []
    pp = 7830457
    for p in pows:
        while pp >= p:
            pp = pp - p
            powers.append(p)

    s = 1
    for p in powers:
        a = pow_of_twos[p]
        s = (s * a) % limit

    s = (s*28433) % limit
    s = (s + 1) % limit
    return s
