# -*- coding: utf-8 -*-

__title__ = "Arranged probability"

def solve():

    # The Pell eq: x^2 - d y^2 = 1
    # The negative Pell equation: x*x - d*y*y = -1

    # blue disc number: b
    # total disc : n
    # b*(b-1)*2 = n(n-1)
    #   2*(2b-1)^2 = (2n-1)^2 +1
    #   if x = 2n-1, y = 2b-1
    #   xx - 2yy = -1

    #xx-2yy = -1
    def get_solution1():
        limit = 10
        for x in xrange(1, limit+1):
            for y in xrange(1, x+1):
                p1 = x*x
                p2 = 2*y*y
                if p1 == p2 - 1:
                    return (x, y)
                elif p1 < p2 - 1:
                    break

    #xx-2yy = 1
    def get_solution2():
        limit = 10
        for x in xrange(1, limit+1):
            for y in xrange(1, x+1):
                p1 = x*x
                p2 = 2*y*y
                if p1 == p2 + 1:
                    return (x, y)
                elif p1 < p2 + 1:
                    break

    from common import log

    x1, y1 = get_solution2()
    xi, yi = get_solution1()

    while True:
        xj = x1*xi + 2*y1*yi
        yj = x1*yi + y1*xi

        xi, yi = xj, yj
        log([(xi+1)/2, (yi+1)/2])
        if (xi+1)/2 > 10**12:
            return (yi+1)/2


