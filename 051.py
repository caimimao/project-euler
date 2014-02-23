
__title__ = "Prime digit replacements"

def solve():
	from common.util import get_prime_below_seive, isprime
	from math import sqrt
	from common import log

	limit = 1000000
	seive = get_prime_below_seive(limit)
	primes = filter(None, seive)

	def is_a_prime(n):
		if n >= limit:
			return isprime(n)
		else:
			return seive[n] != 0	

    #TODO
