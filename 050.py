
__title__ = "Consecutive prime sum"

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

	i = 0
	l = len(primes)
	m = 0
	#l = 1000
	limit = 1000000
	result = ""
	for i in range(0, l):
		s = primes[i]
		if i+m > l:
			break
		if m*s > limit:
			break
		j = i + 1
		while j < l:
			s = s + primes[j]
			if s > limit:
				break
			else:
				if is_a_prime(s) and s <= limit:
					if j - i > m:
						m = j - i 
						log([primes[i], '--', primes[j], s, m])
						result = s

			j = j + 1

	return result

