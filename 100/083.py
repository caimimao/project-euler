# -*- coding: utf-8 -*-

__title__ = "Path sum: four ways"

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

    file = open("data/081.txt", "r")
    data = file.read()
    data = data.split("\n")
    data = [[int(n) for n in line.split(",")] for line in data]

    def printd2(d, n, m):
        for i in range(0, n):
            for j in range(0, m):
                print "%4d" % d[i*n+j],
            print ""
        print ""

    from common import log

    def calc(d, n, m):

        score = [0] * (n*m)

        def test(i, j):
            if i>=0 and i<n and j>=0 and j<m:
                return True
            return False

        def next_point(x1, y1, x2, y2, ps):
            if test(x2, y2):
                if score[x2*n+y2] == 0:
                    score[x2*n+y2] = score[x1*n+y1] + d[x2][y2]
                    ps.append((x2, y2))
                else:
                    if score[x1*n+y1] + d[x2][y2] < score[x2*n+y2]:
                        score[x2*n+y2] = score[x1*n+y1] + d[x2][y2]
                        ps.append((x2, y2))   

        ps1 = [(0, 0)]
        score[0] = d[0][0]

        #printd2(score, n, m)
        while len(ps1)>0:
            ps2 = []
            for x, y in ps1:
                next_point(x, y, x+1, y, ps2)
                next_point(x, y, x, y+1, ps2)
                next_point(x, y, x-1, y, ps2)
                next_point(x, y, x, y-1, ps2)

            ps1 = ps2
            #printd2(score, n, m)

        return score[(n-1)*n+(m-1)]

    log(calc(d, 5, 5))
    return calc(data, 80, 80)




