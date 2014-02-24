# -*- coding: utf-8 -*-

__title__ = "Minimal network"

def solve():

    from common import log
    file = open("data/107.txt", 'r')
    data = file.read()

    data = data.split("\n")
    grid = []
    ss = 0
    for line in data:
        row = []
        for s in line.split(","):
            if s != '-':
                row.append(int(s))
            else:
                row.append(0)
        grid.append(row)
        ss = ss + sum(row)

    ss = ss/2

    log("origin = %d" % ss)
    # Kruskal
    U = []

    limit = len(grid[0])

    def dis_cmp(u1, u2):
        return cmp(u1[2], u2[2])

    for i in xrange(0, limit):
        for j in xrange(i+1, limit):
            if grid[i][j] > 0:
                U.append((i, j, grid[i][j]))

    def span(v):
        for i in xrange(1,limit):
            if v[i] != v[0]:
                return False
        return True

    def connect(v, i, j):
        m = min(v[i], v[j])
        n = max(v[i], v[j])
        for x in xrange(1,limit):
            if v[x] == n:
                v[x] = m

    U = sorted(U, dis_cmp)

    V = [i for i in xrange(0, limit)]

    min_ss = 0
    for u in U:
        if V[u[0]] == V[u[1]]:
            continue
        connect(V, u[0], u[1])
        log(" ".join(["%s" % chr(x+ord('A')) for x in V]))
        min_ss = min_ss + u[2]
        if span(V):
            return ss - min_ss
