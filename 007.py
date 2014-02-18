__title__ = "10001st prime"

def solve():
	from common.math import get_prime_list
	primes = get_prime_list(10001)
	return primes[-1]