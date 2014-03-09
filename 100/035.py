
__title__ = "Circular primes"

def solve():
	from common.util import get_prime_below_seive
	from common import log

	limit = 1000001
	seive = get_prime_below_seive(limit)
	primes = filter(None, seive)

	def get_digits(p):
		digits = []
		while p>0:
			p, m = divmod(p, 10)
			digits.insert(0, m)
		return digits

	def prefilter(p):
		l = get_digits(p)
		return any(map(lambda x: x%2==0, l))

	def get_rotations(p):
		digits = get_digits(p)
		for d in xrange(1, len(digits)):
			yield int(''.join(map(str, (digits[d:] + digits[0:d]))))

	s = 0
	for p in primes:
		if not prefilter(p):
			found = True
			for next in get_rotations(p):
				if seive[next] == 0:
					found = False
					break
			if found == True:
				s = s + 1
				log(p)

	return s + 1 # 2


