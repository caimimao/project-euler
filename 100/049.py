
__title__ = "Prime permutations"

def solve():

	from common.util import get_prime_below_seive, isprime
	from math import sqrt
	from common import log

	limit = 10001
	seive = get_prime_below_seive(limit)
	primes = filter(None, seive)

	def is_a_prime(n):
		if n >= limit:
			return isprime(n)
		else:
			return seive[n] != 0
	
	def get_num(n):
		s = set()
		return set(str(n))

	result = []
	for p in primes:
		if p > 999:
			s1 = get_num(p)
			for q in primes:
				if q > p and get_num(q) == s1:
					# r - q = q - p 
					# r = 2q -p

					if 2*q-p<9999 and get_num(2*q-p) == s1 and is_a_prime(2*q-p):
						log([p, q, 2*q-p])
						if p != 1487:
							result = [p, q, 2*q-p]

	return "".join(map(str, result))
