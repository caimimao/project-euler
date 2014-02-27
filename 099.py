# -*- coding: utf-8 -*-

__title__ = ""

def solve():
    file = open("data/099.txt", "r")
    data = file.read()
    data = data.split("\n")
    data = [line.split(",") for line in data]

    grid = []
    no = 1
    for line in data:
        newline = [no] + [int(x) for x in line]
        grid.append(newline)
        no = no + 1

    from math import log10

    for line in grid:
        c = line[2]*log10(line[1])
        line.append(c)

    def mycmp(x, y):
        return cmp(x[3], y[3])

    grid.sort(mycmp)
    from common import log
    for no, a, b, c in grid:
        log("%4d, %8d^%8d ~ 10^(%10.10f)" % (no, a, b, c))

    return grid[-1][0]



