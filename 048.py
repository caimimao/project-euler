# -*- coding: utf-8 -*-
__title__ = "Self powers"

__doc__ = """
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

def solve():

	s = 0
	limit = 10**12
	for i in range(1, 1001):
		p = 1
		for j in range(1, i+1):
			p = p * i % limit
		s = (s + p)  % limit

	return str(s)[-10:]


