# -*- coding: utf-8 -*-

__title__ = "Non-bouncy numbers"

def solve():

    #increasing
    # f (n, d) is number of increasing number which start with d and have n-digits
    #  where d in [1, 9]
    #  1xxx, 2xxx, 3xxx, ..., 9xxx -> 11xxx, 12xxx, 13xxx, ..., 19xxx
    #        2xxx, 3xxx, ..., 9xxx -> 22xxx, 23xxx, ..., 29xxx
    #              3xxx, ..., 9xxx -> 33xxx, ..., 19xxx
    #                           .....
    #                         9xxx -> 99xxx
    #  f(n, d) = SUM(f(n-1, e)) for 9 => e >= d

    # decreasing
    # g (n, d) is number of decreasing number which end with d and have n-digits
    #   where d in [0, 9]
    #  xxx0, xxx1, xxx2, ..., xxx9 -> xxx00, xxx10, xxx20, ..., xxx90
    #        xxx1, xxx2, ..., xxx9 -> xxx11, xxx21, ..., xxx91
    #              xxx2, ..., xxx9 -> xxx22, ..., xxx92
    #                           .....
    #                         xxx9 -> xxx99
    # g (n, d) = SUM(g(n-1, e)) for 9-d => e >= 0

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

    log(get_non_bouncy_number(6))  #below 1000000
    log(get_non_bouncy_number(10))  #below 10^10
    s = get_non_bouncy_number(100)  #below 10^100
    log(s)
    return s










