# -*- coding: utf-8 -*-
__title__ = "Champernowne's constant"

__doc__ = """

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def solve():
	# 1-9        > 10^1-10^0  
	# 10-99      > 10^2-10^1
	# 100-999    > 10^3-10^2
	# 1000-9999  > 10^4-10^3

	from common import log
	
	def f(n):
		return (10**n - 10**(n-1))*n

	fn = [f(i) for i in range(1, 7)]
	#print fn

	def d(n):
		if n == 1:
			return 1
		index = 0
		s = fn[0]

		while n>s:
			index = index + 1
			s = s + fn[index]
		m = index + 1
		n = n - sum(fn[0:m-1])
		order, pos = divmod(n, m)
		#print (n, m, order, pos, str(10**(m-1) + order))
		return int(str(10**(m-1) + order)[pos-1])

	dd = 1
	for i in range(0, 7):
		dd = dd * d(10**i)
		log("d(%10d) = %d" % (10**i, d(10**i)))

	return dd
