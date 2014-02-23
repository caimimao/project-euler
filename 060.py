# -*- coding: utf-8 -*-

__title__ = "Prime pair sets"

def solve():
    from common.util import get_prime_below_seive, isprime
    from math import sqrt
    from common import log

    limit = 10000
    limit_pow = limit*limit
    seive = get_prime_below_seive(limit)
    primes = filter(None, seive)

    def is_a_prime(n):
        if n >= limit:
            if n<limit_pow:
                from math import sqrt
                root = sqrt(n) + 1
                for p in primes:
                    if p > root:
                        break
                    if n % p == 0:
                        return False
                return True
            else:
                return isprime(n)
        else:
            return seive[n] != 0

    def get(x,y):
        return int(str(x) + str(y))

    def match(x, y):
        if is_a_prime(get(x, y)) and is_a_prime(get(y, x)):
            return True
        else:
            return False

    print '-------'
    n = len(primes)
    n = 1200
    print primes[1200]
    g = [[] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(i+1, n):
            if match(primes[i],primes[j]):
                #print (primes[i],primes[j])
                g[i].append(j)


    ans = 1000000000
    p = primes
    for a in xrange(0, n):
        if p[a]*5 > ans:
            break
        for ta in xrange(0, len(g[a])):
            b = g[a][ta]
            if p[a] + p[b]*4 > ans:
                break
            for tb in xrange(0, len(g[b])):
                c = g[b][tb]
                if p[a] + p[b] + p[c]*3 > ans:
                    break
                if not match(p[a], p[c]):
                    continue
                for tc in xrange(0, len(g[c])):
                    d = g[c][tc]
                    if p[a] + p[b] + p[c] + p[d]*2 > ans:
                        break
                    if not match(p[d], p[a]):
                        continue
                    if not match(p[d], p[b]):
                        continue
                    for td in xrange(0, len(g[d])):
                        e = g[d][td]
                        if p[a] + p[b] + p[c] + p[d] + p[e] > ans:
                            break
                        if not match(p[e], p[a]):
                            continue
                        if not match(p[e], p[b]):
                            continue
                        if not match(p[e], p[c]):
                            continue

                        s = sum([p[a], p[b], p[c], p[d], p[e]])
                        if s < ans:
                            ans = s 
                            log("number:%s, sum:%d" % ([p[a], p[b], p[c], p[d], p[e]], s))

    return ans





