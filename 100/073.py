# -*- coding: utf-8 -*-

__title__ = "Counting fractions in a range"

def solve1():
    from common.util import gcd
    limit = 12000

    # n/d > 1/3 and n/d < 1/2
    #  d/2 >  n > d/3
    result = 0
    for d in xrange(5, limit+1):
        for n in xrange(int(d/3), int(d/2)):
            if gcd(n, d) == 1:
                result = result + 1

    return result

def solve2():
    # Farey Sequences
    # Ref http://www.mathblog.dk/project-euler-73-sorted-reduced-proper-fractions/
    # Ref http://en.wikipedia.org/wiki/Farey_sequence

    limit = 12000
    a, b = 1, 3
    c, d = 4000, 11999

    result = 0
    while ( c!=1 or d !=2 ):
        result = result + 1
        k = int ((limit + b) / d)
        e = k * c - a
        f = k * d - b
        a, b = c, d
        c, d = e, f

    return result


def solve():
    return solve2()