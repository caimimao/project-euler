# -*- coding: utf-8 -*-

__title__ = ""

def solve():
    
    def sum_of_digits(n):
        return sum(map(int, str(n)))
 
    a = []
    n = 30
    for x in range(2, 100):
        for e in range(2, 25):
            p = x**e
            if sum_of_digits(p) == x: 
                a.append(p)
 
    a.sort()
    return a[n-1]
