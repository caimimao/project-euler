# -*- coding: utf-8 -*-

__title__ = "Square root convergents"

def solve():
    # A(n) = M(n)/D(n)
    # A(n) = 1/[2+A(n-1)]
    # ==> M(n) = 2*D(n-1) + M(n-1)
    #     D(n) = D(n-1) + M(n-1)

    from common import log
    from common.util import gcd
    m = [3]
    d = [2]

    def next(n):
        tmp2 = d[n-1] + m[n-1]
        tmp1 = tmp2 + d[n-1]
        c = gcd(tmp1, tmp2)
        m.append(tmp1//c)
        d.append(tmp2//c)

    count = 0
    for i in range(1, 1000):
        next(i)
        if len(str(m[i]))>len(str(d[i])):
            count = count + 1

    return count




