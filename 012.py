__title__ = "Highly divisible triangular number"

from common.math import get_prime_below
from common import log

def solve():
	primes = get_prime_below(2000000)

	def count_of_divisor(number):
		count = 1
		for i in primes:
			c = 1
			while number % i == 0:
				number = number/i
				c = c + 1
			count = count*c
			if number == 1:
				return count
		if number>20000000:
			print "error"
		return 2

	triangle = 28
	triangle_index = 7

	count = count_of_divisor(triangle)
	while count<=500:
		triangle_index = triangle_index + 1
		triangle = triangle + triangle_index
		count = count_of_divisor(triangle)
		#print "count: %d of %d" % (count, triangle)
	return triangle

