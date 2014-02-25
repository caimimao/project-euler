# -*- coding: utf-8 -*-

__title__ = "Ordered fractions"

def solve():
    from common import log
    a = 3
    b = 7

    # n/m < a/b --> nb <= am - 1
    # n = int(am-1/b)

    nn, mm = 1, 3
    for m in xrange(4, 10**6+1):
        n = int((a*m-1)*1.0/b)

        # n/i > nn/mm
        if n*mm > m*nn:
            nn, mm = n, m

    log([nn, mm])
    return nn


