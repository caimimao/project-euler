
__title__ = "Distinct powers"

def solve():

	from common import log
	limit = 100
	test = {}
	for a in range(2, limit+1):
		for b in range(2, limit+1):
			c = a**b
			if a**b <= limit:
				if not test.has_key(c):
					test[c] = (a, b)
			else:
				break
	log(test)

	double = []
	s = 0
	for a in range(2, limit+1):
		for b in range(2, limit+1):
			if a in test:
				m, n = test[a] #a=m**n

				if b*n<=limit:
					s = s + 1
				else:
					if (m, b*n) in double:
						s = s + 1
					else:
						double.append((m, b*n))
	return 99*99 - s
