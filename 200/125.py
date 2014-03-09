# -*- coding: utf-8 -*-

__title__ = "Palindromic sums"

def solve():
    from math import sqrt
    limit = 10**8
    #limit = 1000
    root = int(sqrt(limit))+1


    squares = [i*i for i in range(1, root)]

    def test(s):
        d = str(s)
        l = len(d)
        for i in range(0, l):
            if d[i] != d[l-i-1]:
                return False
            if l-i-1<=i:
                return True

    l = len(squares)
    result = 0
    map = {}
    for i in range(0, l):
        s = squares[i]
        for j in range(i+1, l):
            s = s + squares[j]
            if s >= limit:
                break
            if test(s):
                if map.has_key(s):
                    print s
                else:
                    #print s, i, j
                    map[s] = 1
                    result = result + s
    return result




