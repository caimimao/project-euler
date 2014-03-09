# -*- coding: utf-8 -*-

__title__ = "Counting summations"

def solve():

    #same with problem 31

    coins = range(99, 0, -1)
    l = len(coins)

    count = 1
    p = 100
    hash = {}
    def get_comb(p, r):
        if hash.has_key((p, r)):
            return hash[(p, r)]
        if p == 1 or r+1 == l:
            hash[(p, r)] = 1
            return 1

        test = p
        s = 0
        coin = coins[r]
        num = get_comb(test, r+1)
        s = s + num
        while test >= coin:
            test = test - coin
            if test == 0:
                s = s + 1
            else:
                num = get_comb(test, r+1)
                s = s + num
        
        hash[(p, r)] = s     
        return s

    return get_comb(100, 0)
