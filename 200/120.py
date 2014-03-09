# -*- coding: utf-8 -*-

__title__ = "Square remainders"

def solve():

    # (n-1)^m + (n+1)^m % n^2
    #    = (n-1)^m % n^2 + (n+1)^m % n^2

    # if m = 2x
    #    = 2
    # if m = 2x + 1
    #    = 2*m*n

    # then if n=2y,   m = 2y-1
    #         n=2y+1, m = 2y-1

    from common import log
    s = 0
    for i in range(3, 1001):
        if i % 2 == 0:
            a = i*(i-2)
        else:
            a = i*(i-1)
        log([i, a])
        s = s + a

    return s


