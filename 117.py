# -*- coding: utf-8 -*-

__title__ = "Red, green, and blue tiles"

def solve():

    #red 2
    #green 3
    #blue 4

    # f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4)
    #   [n-1] --> [n-1]B
    #   [n-2] --> [n-2]RR
    #   [n-3] --> [n-3]GGG
    #   [n-4] --> [n-2]BBBB

    # f(0) = 1   #
    # f(1) = 1   #O
    # f(2) = 2   #OO, RR
    # f(3) = 4   #OOO,ORR,RRO,GGG
    # f(4) = 8   #OOOO,ORRO,RROO,GGGO,OORR,RRRR,OGGG,BBBB

    def f(n):
        ff = [1, 1, 2, 4, 8] + [0]*100
        for i in range(5, n+1):
            ff[i] = ff[i-1] + ff[i-2] + ff[i-3] + ff[i-4]
        return ff[n]

    return f(50)