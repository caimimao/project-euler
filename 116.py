# -*- coding: utf-8 -*-

__title__ = "Red, green or blue tiles"

def solve():

    #red 2
    #green 3
    #blue 4

    # f(m, n) = f(m, n-1) + f(m, n-m) + 1
    #   [n-1] --> [n-1]B
    #   [n-m] --> [n-m]R..R
    #   [B..B]--> [B..B]R..R
    def f(m, n):

        ff = [0]*100
        for i in range(0, m):
            ff[i] = 0
        ff[m] = 1

        for i in range(m+1, n+1):
            if i-m >=0:
                ff[i] = ff[i-1] + ff[i-m] + 1
            else:
                ff[i] = ff[i-1]
        return ff[n]

    print f(2,50) + f(3, 50) + f(4, 50)


