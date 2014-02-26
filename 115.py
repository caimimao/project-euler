# -*- coding: utf-8 -*-

__title__ = "Counting block combinations II"

def solve():
    # R(m, n), number for all ways with right one block is red
    # B(m, n), number for all ways with right one block is black
    # F(m, n) = R(m, n) + B(m, n)

    # R(m, n) = R(m, n-1) + B(m, n-m)
    #    [n-1]R --> [n-1]RR
    #    [n-m-1]BR..R --> [n-m-1]BR..R
    # B(m, n+1) = R(m, n) + B(m, n)
    #    [n-1]R --> [n-1]RB
    #    [n-1]B --> [n-1]BB

    def f(m, limit):
        n = 1
        r = [0] * 500
        b = [1] * 500
        r[1], b[1] = 0, 1
        while True:
            n = n + 1
            # R(m, n) = R(m, n-1) + B(m, n-m)
            if n-m>=0:
                r[n] = r[n-1] + b[n-m]
            else:
                r[n] = r[n-1]
            b[n] = b[n-1] + r[n-1]
            if r[n]+b[n] > limit:
                return n

    from common import log
    limit = 1000000
    s = f(3, limit)
    log(s)
    s = f(50, limit)
    log(s)

    return s


