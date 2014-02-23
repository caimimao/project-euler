# -*- coding: utf-8 -*-

__title__ = "Powerful digit sum"

def solve():
    
    from common import log

    def get_sum(arr):
        s = 0
        for n in arr:
            while n > 0:
                n, m = divmod(n, 10)
                s = s + m
        return s

    smax = 0
    snumber = None
    for a in range(2, 100):
        arr = [a]
        for b in range(2, 100):
            l = len(arr)
            extra = 0
            for j in range(0, l):
                tmp = arr[j]*a + extra
                extra, arr[j] = divmod(tmp, 10000)

            while extra>0:
                arr.append(0)
                extra, arr[-1] = divmod(extra, 10000)

            s = get_sum(arr)
            if s>smax:
                smax = s
                snumber = arr

    return smax

