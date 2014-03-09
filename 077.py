# -*- coding: utf-8 -*-

__title__ = "Prime summations"

def solve():

    #same with problem 31
    from common.util import get_prime_below_seive, isprime
    from math import sqrt
    from common import log

    limit = 200
    limit_pow = limit*limit
    seive = get_prime_below_seive(limit)
    primes = filter(None, seive)

    coins = primes[0:20]
    coins.reverse()
    l = len(coins)

    count = 1
    hash = {}
    def get_comb(p, r):
        if hash.has_key((p, r)):
            return hash[(p, r)]
        if p == 1 or r+1 == l:
            if p % 2 == 0:
                hash[(p, r)] = 1
                return 1
            else:
                hash[(p, r)] = 0
                return 0

        test = p
        s = 0
        coin = coins[r]
        num = get_comb(test, r+1)
        s = s + num
        while test >= coin:
            test = test - coin
            if test <= 0:
                if test == 0:
                    s = s + 1
            else:
                num = get_comb(test, r+1)
                s = s + num
        
        hash[(p, r)] = s     
        return s

    n = 2
    while True:
        num = get_comb(n, 0)
        if num > 5000:
            return n
        n = n + 1
