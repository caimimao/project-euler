
__title__ = "Truncatable primes"

def solve():
	from common.util import get_prime_below_seive
	from common import log

	limit = 1000001
	seive = get_prime_below_seive(limit)
	primes = filter(None, seive)

	all_primes = []


	while len(primes1)>0:
		primes2 = []
		for i in primes1:
			for j in range(1, 10):
				p = i*10+j
				test = True
				if seive[p] == 0:
					test = False
				m = 10
				q = p % m
				if seive[q] == 0:
					test = False
				while q != p:
					m = m * 10
					q = p % m
					if seive[q] == 0:
						test = False

				if test:
					primes2.append(p)
					all_primes.append(p)
					print p
		primes1 = primes2

	print all_primes


