# -*- coding: utf-8 -*-

__title__ = "Digit factorial chains"

def solve():
    
    def factorial(n):
        if n ==0 :
            return 1
        p = 1
        for i in range(1, n+1):
            p = p*i
        return p

    p = [factorial(i) for i in range(0, 10)]

    def f(n):
        d = []
        while n>0:
            n, m = divmod(n, 10)
            d.append(m)
        return sum([p[j] for j in d])



    limit = 1000000

    all_numbers = {}

    def find_chain_length(n):
        chain = [n]
        while True:
            next = f(chain[-1])
            l = len(chain)
            if all_numbers.has_key(next) and all_numbers[next] > 0:
                all_numbers[n] = l + all_numbers[next]
                #print (n, l+1, chain, '*')
                return 

            for i in xrange(l-1, -1, -1):
                if chain[i] == next:
                    all_numbers[n] = l
                    #print (n, l, chain)
                    for j in xrange(i, l):
                        if all_numbers.has_key(chain[j]) and all_numbers[chain[j]] == 0:
                            all_numbers[chain[j]] = l - i + 1
                            #print (n, l, chain[i:l], '**')
                        #print chain
                    return
            chain.append(next)
            #print chain

    n = 0
    while n < limit -1:
        n = n + 1
        if all_numbers.has_key(n) and all_numbers[n]>0:
            continue
        find_chain_length(n)
        #print n

    count = 0
    for i in all_numbers.keys():
        if i < limit and all_numbers[i]>=60:
            count = count + 1

    return count
