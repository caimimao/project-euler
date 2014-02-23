# -*- coding: utf-8 -*-

__title__ = "Cubic permutations"

def solve():
    
    cubes = {}

    n = 345

    def get_larget_perm(n):
        k = n
        ret = 0
        digits = [0 for i in xrange(0, 10)]
        while k>0:
            k, m = divmod(k, 10)
            digits[m] = digits[m] + 1

        for i in xrange(9, -1, -1):
            for j in xrange(0, digits[i]):
                ret = ret * 10 + i

        return ret

    while True:
        n = n + 1

        largest_perm = get_larget_perm(n*n*n)
        if not cubes.has_key(largest_perm):
            cubes[largest_perm] = [n, 1, [n, n*n*n]]
        else:
            cubes[largest_perm][1] = cubes[largest_perm][1] + 1
            cubes[largest_perm][2].append(n)
            cubes[largest_perm][2].append(n*n*n)
            if cubes[largest_perm][1] == 5:
                return cubes[largest_perm][2][1]

