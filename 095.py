# -*- coding: utf-8 -*-

__title__ = "Amicable chains"

def solve():
    limit = 1000000

    from math import sqrt
    from common import log

    sums = [1 for i in range(0, limit+1)]
    for i in range(2, limit):
        step = i + i
        while step < limit:
            sums[step] = sums[step] + i
            step = step + i

    def sum_of_divisors(n):
        return sums[n]

    for i in range(2, 10):
        print i, sum_of_divisors(i), sums[i]

    chains = [None for i in range(0, limit+1)]
    max_length = 0
    min_number = 0
    for i in range(12496, limit+1):
        if chains[i] == None and sums[i]<limit:
            chain = [i]
            next = sum_of_divisors(i)

            looped = False
            while True:
                if next >= limit:
                    break
                if next == i:
                    looped = True
                    break
                if next in chain:
                    break
                if looped:
                    break
                if next < i:
                    break
                chain.append(next)
                next = sum_of_divisors(next)

            for n in chain:
                chains[n] = "Jump"
            if looped:
                chains[i] = chain

                if len(chain) > max_length:
                    max_length = len(chain)
                    log(chain)
                    min_number = chain[0]
            else:
                chains[i] = "Jump-Broken"

    return min_number
