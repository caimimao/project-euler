__title__ = "10001st prime"

def solve():
	from common.math import get_prime_below
	primes = get_prime_below(200000)
	return primes[10000]