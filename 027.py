
__title__ = "Quadratic primes"

def solve():
	from common import log
	from common.util import get_prime_below, get_prime_below_seive
	# f(n)   = n*n + an + b
	# f(n+1) = (n+1)(n+1) + a(n+1) + b
	#        = (n^2 + an + b) + 2n + 1 + a
	#        = f(n) + 2n + 1 + a
	# f(0)   = b
	limit = 10000
	primes_map = get_prime_below_seive(limit)
	def fn(n, a, b):
		return n*n + a*n + b

	def count(a, b):
		from common.util import isprime
		if not isprime(b):
			return 0
		next = True
		n = 0
		f = b
		while next:
			n = n+1
			f = 2*n-1+a+f
			#f = fn(n, a, b)
			if f <= 0 :
				return n

			if f < limit :
				if primes_map[f] == 0:
					return n
			else:
				if not isprime(f):
					return n 
				#print f



	c_max = 0
	for a in range(-999, 1000):
		for b in range(2, 1000):
			c = count(a, b)
			if c > c_max:
				log("%3d,%3d=%5d" % (a, b, count(a, b)))
				c_max = c
				p_max = a*b

	return p_max






