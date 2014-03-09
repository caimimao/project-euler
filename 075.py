# -*- coding: utf-8 -*-

__title__ = "Singular integer right triangles"

def solve():
    limit = 1500000

    count = {}

    result =0
    from math import sqrt
    from common.util import gcd
    mlimit = int(sqrt(limit/2))

    for m in xrange(2, mlimit+1):
        for n in xrange(1, m):
            if (n+m) % 2 == 1 and gcd(n, m) == 1:
                #a = m*m + n*n
                #b = m*m - n*n
                #c = 2*m*n
                #p = a + b + c
                step = 2*m*(m+n)
                p = step
                while p <= limit:
                    if count.has_key(p):
                        if count[p] == 1:
                           result = result - 1 
                        count[p] = count[p] + 1
                    else:
                        count[p] = 1
                        result = result + 1
                    p = p + step


    return result