
__title__ = "Goldbach's other conjecture"

def solve():

	from common.util import get_prime_below_seive, isprime
	from math import sqrt
	from common import log

	limit = 10000
	seive = get_prime_below_seive(limit)
	primes = filter(None, seive)

	def is_a_prime(n):
		if n >= limit:
			return isprime(n)
		else:
			return seive[n] != 0


	def test(n):
		if is_a_prime(n):
			return True

		for p in range(2, n-2):
			if is_a_prime(p):
				d, m = divmod(n-p, 2)
				if m == 0:
					k = int(sqrt(d))
					if k*k == d:
						log("%d = %d + %d^2" % (n, p, k))
						return True
		return False

	start = 35

	while test(start):
		start = start + 2

	return start