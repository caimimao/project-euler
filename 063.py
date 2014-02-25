# -*- coding: utf-8 -*-

__title__ = "Powerful digit counts"

def solve():
    from common import log
    def count(n):
        s = 0
        while n > 0:
            n, m = divmod(n, 10)
            s = s + 1
        return s

    s = 0
    for i in xrange(1, 10):
        n = 1
        while True:
            a = pow(i, n)
            c = count(a)
            if c == n:
                s = s + 1
                log("%s = %d" % ((i, n), a))
            if n > 20:
                break
            n = n + 1

    return s





