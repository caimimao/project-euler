# -*- coding: utf-8 -*-
__title__ = "Integer right triangles"

__doc__ = """
If p is the perimeter of a right angle triangle with integral 
length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def solve():
	from common import log
	# a + b + c = n
	# a*a + b*b = c*c
	# ==> a*a + b*b = (n-a-b)(n-a-b)= n*n + a*a + b*b - 2an -2bn + 2ab
	# ==> 0 = n*n - 2an + 2ab - 2bn
	# ==> n(n-2a) = 2b(n-a)
	result = []
	for n in range(4, 1001, 2):
		count = 0
		for a in range(1, n/2 + 1):
			x = n*(n-2*a)
			y = 2*(n-a)
			if x>y and x % y == 0 :
				count = count + 1
				if count == 1:
					log("---------------------------------")
					log("n = %d " % n)
				log(str((a, x//y, n-a-x//y)))
		if count>0:
			result.append((count, n))

	result.sort()
	return result[-1][1]
