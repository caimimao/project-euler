__title__ = "10001st prime"

def solve():
	from common.util import get_prime_below
	primes = get_prime_below(200000)
	return primes[10000]