# -*- coding: utf-8 -*-

__title__ = "Pandigital Fibonacci ends"

# Ref: http://blog.singhanuvrat.com/problems/get-first-few-digits-of-a-fibonacci-number

def solve():
    from common import log

    def first_digits_of_fib(n, d):
        temp = n * 0.20898764024997873 - 0.3494850021680094
        return int( pow( 10, temp - int( temp ) + d - 1 ) )

    def is_pandigital(k):
        x = [-1 for i in range(0, 9)]
        while k>0:
            k, m = divmod(k, 10)
            if m > 0:
                x[m-1] = 1
        return x.count(-1) == 0


    f1 = 1
    f2 = 1
    k = 3
    while True:
        tmp = f2
        f2 = (f1 + f2) % 1000000000
        f1 = tmp
        if is_pandigital(f2):
            if is_pandigital(first_digits_of_fib(k, 9)):
                log(f2)
                log(first_digits_of_fib(k, 9))
                return k
        k = k + 1

