# -*- coding: utf-8 -*-

__title__ = "Counting block combinations I"

def solve():


    # Red(n), number for all ways with right one block is red
    #    [n-1]R
    # Black(n), number for all ways with right one block is black
    #    [n-1]B

    # Red(n+1) = Red(n) + Black(n-2)
    #    [n-1]R --> [n-1]RR
    #    [n-3]BRR --> [n-3]BRRR
    # Black(n+1) = Red(n) + Black(n)
    #    [n-1]R --> [n-1]RB
    #    [n-1]B --> [n-1]BB

    r = [0] * 51
    b = [0] * 51

    n = 3
    # BBB
    # RRR
    r[3], b[3] = 1, 1

    n = 4
    # BBBB
    # RRRB
    # BRRR
    # RRRR
    r[4], b[4] = 2, 2

    n = 5
    # BBBBB
    # RRRBB
    # BRRRB
    # RRRRB
    # BBRRR
    # BRRRR
    # RRRRR
    r[5], b[5] = 3, 4

    from common import log
    for n in range(6, 51):
        r[n] = r[n-1] + b[n-3]
        b[n] = r[n-1] + b[n-1]
        log("%2d -- %d" % (n, r[n] + b[n]))


    return r[50]+b[50]
