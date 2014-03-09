# -*- coding: utf-8 -*-

__title__ = "Path sum: three ways"

def solve():
    #test data
    d = [
    [131,673,234,103, 18],
    [201, 96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524, 37,331],
    ]

    def printd(d, n, m):
        for j in range(0, n):
            print d[j]
        print ""

    def calc(d, n, m):
        #printd(d, n, m)
        for j in range(1, m):
            dj = [d[k][j] for k in range(0, n)]
            for i in range(0, n):
                if i == 0:
                    d[i][j] = dj[i] + d[i][j-1]
                if i > 0:
                    d[i][j] = dj[i] + min(d[i][j-1], d[i-1][j])
            for i in range(n-1, -1, -1):
                if i == n - 1:
                    d[i][j] = d[i][j]
                if i < n - 1:
                    d[i][j] = min(d[i][j], dj[i]+d[i+1][j])
            #printd(d, n, m)

        line = [d[i][m-1] for i in range(0, n)]
        return min(line)

    file = open("data/081.txt", "r")
    data = file.read()
    data = data.split("\n")
    data = [[int(n) for n in line.split(",")] for line in data]

    from common import log
    log(calc(d, 5, 5))
    return calc(data, 80, 80)
