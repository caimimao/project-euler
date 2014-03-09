# -*- coding: utf-8 -*-

__title__ = "Ordered radicals"

def solve():
    limit = 100000
    n = [[1, i] for i in range(1, limit+1)]

    #seive
    for i in range(1, limit+1):
        if n[i-1][0] == 1:
            step = i
            while step <=limit:
                n[step-1][0] = i*n[step-1][0]
                step = step + i

    n.sort()
    return n[9999][1]

