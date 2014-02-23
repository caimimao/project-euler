
__title__ = "Distinct primes factors"

def solve():
	
	from common.util import get_prime_below_seive, isprime
	from math import sqrt
	from common import log

	limit = 100000
	seive = get_prime_below_seive(limit)
	primes = filter(None, seive)

	def is_a_prime(n):
		if n >= limit:
			return isprime(n)
		else:
			return seive[n] != 0	

	def get_count(n):

		origin = n
		if is_a_prime(n):
			return (1, [n])

		count = 0
		factors = []
		for p in primes:
			if n % p == 0:
				count = count + 1
				factors.append(p)
				n = n // p
				while n % p == 0:
					n = n // p
			if n == 1:
				return (count, factors)
				

		if n > primes[-1]:
			if is_a_prime(n):
				count = count + 1
				factors.append(n)
				return (count, factors)

			for p in range(primes[-1], int(sqrt(n))):
				if is_a_prime(p):
					if n % p == 0:
						count = count + 1
						factors.append(p)
						n = n // p
						while n % p == 0:
							n = n // p
					if n == 1:
						return (count, factors)
			print n


	start = 2
	while True:
		found = True
		for i in range(0, 4):
			count, factors = get_count(start+i)
			#print (start, count)
			if count != 4:
				found = False
				break

		if found:
			for i in range(0, 4):
				count, factors = get_count(start+i)
				log("%d = %s" % (start+i, factors))
			return start
		else:
			start = start + 1

