# -*- coding: utf-8 -*-

__title__ = "Cyclical figurate numbers"

def solve():

    from common import log
    def p3(n): return n*(1*n+1)/2
    def p4(n): return n*(2*n-0)/2
    def p5(n): return n*(3*n-1)/2
    def p6(n): return n*(4*n-2)/2
    def p7(n): return n*(5*n-3)/2
    def p8(n): return n*(6*n-4)/2

    def generate_numbers(i):
        result = []
        n = 1
        while True:
            pn = n*((i+1)*n-(i-1))/2
            n = n + 1
            if pn >= 1000 and pn <=9999:
                result.append(pn)
            if pn > 9999:
                return result

    numbers = [[] for i in xrange(0, 6)]

    for i in range(0, 6):
        numbers[i] = generate_numbers(i)

    solution = [0 for x in range(0, 6)]
    def find_next(last, length):
        for i in xrange(0, 6):
            if solution[i] != 0:
                continue
            for j in range(0, len(numbers[i])):
                unique = True
                for k in xrange(0, 6):
                    if numbers[i][j] == solution[k]:
                        unique = False
                        break

                if unique:
                    if numbers[i][j]/100 == solution[last] % 100:
                        solution[i] = numbers[i][j]
                        if length == 5:
                            if (solution[5]/100 == solution[i] % 100):
                                return True
                        if find_next(i, length+1):
                            return True
            solution[i] = 0
        return False

    for i in xrange(0, len(numbers[5])):
        solution[5] = numbers[5][i]
        if find_next(5, 1):
            break

    result = sum(solution)
    log(solution)
    return result

