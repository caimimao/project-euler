# -*- coding: utf-8 -*-

__title__ = "Counting rectangles"

def solve():
    
    #c(n+1, 2)*c(m+1, 2)
    # ---> (n+1)*n*(m+1)*m/4

    limit = 2000000

    x = 2000
    y = 1
    result = 0
    error = None

    while x>=y:
        rect = x*(x+1)*y*(y+1)/4

        new_error = abs(rect-limit)
        if error == None or (error>new_error):
            result = x*y
            error = new_error

        if rect > limit:
            x = x - 1
        else:
            y = y + 1

    return result



