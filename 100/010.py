__title__ = "Summation of primes"

from common.util import get_prime_below

def sum_of_list(numbers):
	sum = 0
	for i in numbers:
		sum = sum + i
	return sum

from common import log
def solve():
	primes = get_prime_below(2000001)
	s = sum_of_list(primes)
	log(s)
	return s

