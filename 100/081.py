# -*- coding: utf-8 -*-

__title__ = "Path sum: two ways"

def solve():
    from common import log
    def calc(d, n, m):
        for i in range(0, n):
            for j in range(0, m):

                if i>0 and j>0:
                    d[i][j] = min(d[i-1][j], d[i][j-1]) + d[i][j]
                else:
                    if i==0 and j>0:
                        d[i][j] = d[i][j-1] + d[i][j]
                    if j==0 and i>0:
                        d[i][j] = d[i-1][j] + d[i][j]
        return d[n-1][m-1]

    #test data
    d = [
    [131,673,234,103, 18],
    [201, 96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524, 37,331],
    ]
    log(calc(d, 5, 5))

    file = open("data/081.txt", "r")
    data = file.read()
    data = data.split("\n")
    data = [[int(n) for n in line.split(",")] for line in data]

    return calc(data, 80, 80)
