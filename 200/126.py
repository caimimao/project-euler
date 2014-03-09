# -*- coding: utf-8 -*-

__title__ = "Cuboid layers"

def solve():
    #C(x,y,z,n) = 2(x*y + y*z +  x*z) + 4(x+y+z+n-2)*(n-1)

    def c(x, y, z, n):
        return (x*y+y*z+z*x)*2 + (n-1)*4*(x+y+z+n-2)

    limit = 20000
    zlimit = 100

    map = {}
    x = 1
    while c(x, x, x, 1) < limit:
        y = x 
        while c(x, x, y, 1) < limit:
            z = y
            while c(x, y, z, 1) < limit:
                n = 1
                while c(x, y, z, n) < limit:
                    v = c(x, y, z, n)
                    #print x, y, z, n, v
                    if map.has_key(v):
                        map[v] = map[v] + 1
                    else:
                        map[v] = 1
                    n = n + 1
                z = z + 1
            y = y + 1
        x = x + 1

    for i in sorted(map.keys()):
        if map[i] == 1000:
            return i


