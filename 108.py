# -*- coding: utf-8 -*-

__title__ = "Diophantine reciprocals I"

def solve():
    # 1/x + 1/y = 1/n
    # --> (x-n)(y-n) = n*n

    # set n*n = (p1^k1*p2^k2...pn^kn)^2
    #  O = (2k1+1)*(2k2+1)...*(2kn+1) solutions
    #  int((O+1)/2) if x<=y


    import math
    from common import log

    f = [2,3,5,7,11,13,17,19,23,29,31,37,41.43,47]

    factorNumbers = 13
    limit = 1000

    # build a generator (thanks to Sans SS)
    def genEx(limit):
        output = [1] * 14
        while output[13] < limit:
            i = 13
            while i > 0 and (output[i] == output[i-1]):
                output[i] = 1
                i -= 1
            output[i] += 2
            yield output

    loop = genEx(factorNumbers)

    import operator

    def bigEnough(exps, threshold):
        expandedFactors = reduce(operator.mul, exps)
        if expandedFactors >= threshold:
            return True
        else:
            return False

    def factorExpansion(f, exps):
        output = 1
        for i in range(len(f)):
            output *= math.pow(f[i], exps[i]-1)
        return output
        

    answer = float("inf")
    solution = []

    for i in loop:
        if bigEnough(i, limit*2):
            temp = factorExpansion(f, i)
            if temp < answer:
                answer = temp
                solution = i[:]
                log(answer)
                log(solution)
                log("")

    # for the exponents in our solution list, subtract 1
    # the square root means we take each exponent and divide by 2
    temp = [(x-1)/2 for x in solution]

    answer = 1
    info = []
    for i in range(14):
        answer *= int(math.pow(f[i], temp[i]))
        if temp[i] > 0:
            info.append("%d^%d" % (f[i], temp[i]))
    log(" + ".join(info))

    return answer

