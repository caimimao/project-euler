
# -*- coding: utf-8 -*-
__title__ = "Pandigital multiples"

__doc__ = """
Take the number 192 and multiply it by each of 1, 2, and 3:
  192 × 1 = 192
  192 × 2 = 384
  192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 
192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def solve():
	from common import log

	def get_digits(n):
		d = []
		while n>0:
			n, m = divmod(n, 10)
			d.append(m)
		return d

	def get_pandigital(n, t):
		return "".join(map(lambda i: str(n*i), t))

	result = []
	for i in range(1, 10000):
		n = 1
		p = []
		map_of_num = {}
		quit = False
		while not quit:
			d = get_digits(i*n)
			for j in d:
				if map_of_num.has_key(j) or j == 0:
					quit = True
					break
				else:
					map_of_num[j] = 1
			if not quit:
				n = n + 1
			if len(map_of_num) == 9:
				p = get_pandigital(i, range(1, n))
				log("%d, %s   -  %s" % (i, range(1, n), p))
				result.append(p)

	return result[-1]


