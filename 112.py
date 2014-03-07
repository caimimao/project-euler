# -*- coding: utf-8 -*-

__title__ = "Bouncy numbers"

def solve():
    from common import log
    def get_non_bouncy_number(n):
        ff = [0] + range(9, 0, -1)
        gg = [9] + range(9, 0, -1)

        s = 99 # 1-99 are non bouncy
        m = 3
        while m <= n:
            # f(m, 0) = 0
            f = [0]
            for d in range(1, 10):
                # f(m, d)
                f.append(sum(ff[d:10]))
            g = []
            for d in range(0, 10):
                # g(m, d)
                g.append(sum(gg[d:10]))
            s += sum(f) + sum(g) - 9

            #print f
            #print g
            ff = f
            gg = g
            m = m + 1
        return s

    def is_bouncy(n):
        origin = n
        inc = False
        dec = False
        n, last = divmod(n, 10)
        while n>0:
            n, next = divmod(n, 10)
            if next > last:
                inc = True
            elif next < last:
                dec = True

            last = next
            if dec and inc:
                return True
        return dec and inc
    c = get_non_bouncy_number(6)
    log([c, 100-100.0*c/10**6])

    i = 10**6-1
    count = 10**6-c-1
    while True:
        i = i + 1
        if is_bouncy(i):
            count = count + 1

        if 100*count >= 99*i:
            return i



