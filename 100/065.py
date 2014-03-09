# -*- coding: utf-8 -*-

__title__ = "Convergents of e"

def solve():
    # e = [2; 1,2,1,1,4,1,1,6,1,...,1,2k,1]
    # p(n) = a(n)p(n-1) + p(n-2), p(-1) = 1, p(-2) = 0
    # q(n) = a(n)q(n-1) + q(n-2), q(-1) = 0, q(-2) = 1

    from common import log
    def a(n):
        if n==0:
            return 2
        m = (n + 2) % 3
        if m == 0 or m == 2:
            return 1
        return 2*((n+2) // 3)

    p = [0, 1] + [0 for x in xrange(0, 100)]
    q = [1, 0] + [0 for x in xrange(0, 100)]

    for i in xrange(0, 100):
        p[i+2] = a(i)*p[i+1] + p[i]
        q[i+2] = a(i)*q[i+1] + q[i]
        #log([p[i+2], q[i+2]])

    s = sum(map(int, list(str(p[-1]))))
    return s



