# -*- coding: utf-8 -*-

__title__ = "Darts"

def solve():
    
    from common import log
    #single
    s = range(1,21)
    #double
    d = range(2,42,2)
    #triple
    t = range(3,63,3)
    #bull
    b = [25]
    #double bull
    e = [50] 
    all = s + d + t + b + e
    all_double = d + e



    l = len(all)
    m = len(all_double)

    scores = [0] * 171 # T20, T20, D25

    # x, y, D
    for i in xrange(0, l):
        for j in xrange(i+1, l):
            for k in xrange(0, m):
                s = all[i] + all[j] + all_double[k]
                scores[s] = scores[s] + 1

    # x D and x x D
    for i in xrange(0, l):
        for k in xrange(0, m):
            s = all[i] + all[i] + all_double[k]
            scores[s] = scores[s] + 1
            s = all[i] + all_double[k]
            scores[s] = scores[s] + 1

    # D
    for k in xrange(0, m):
        s = all_double[k]
        scores[s] = scores[s] + 1    


    log(sum(scores))
    log(scores)
    return sum(scores[1:100])




