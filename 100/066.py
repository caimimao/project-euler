# -*- coding: utf-8 -*-

__title__ = "Diophantine equation"

#Ref http://en.wikipedia.org/wiki/Pell%27s_equation

def solve():
    from math import sqrt
    from common import log

    result = 0
    maxx = 0
    for n in xrange(2, 1001):
        root = int(sqrt(n))
        if root*root == n:
            continue

        m, d, a = 0, 1, root

        numm1 = 1
        num = a
        denm1 = 0
        den = 1

        while (num*num - n*den*den != 1):
            m = d*a-m
            d = (n-m*m)/d
            a = int((root + m)/d)

            numm2 = numm1
            numm1 = num

            denm2 = denm1
            denm1 = den

            num = a*numm1 + numm2
            den = a*denm1 + denm2


        if num > maxx:
            log("%3d = x:%d,y:%d" % (n, num, den))
            maxx = num
            result = n
    return result

