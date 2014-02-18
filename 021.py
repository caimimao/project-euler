
__title__ = "Amicable numbers"


def get_divisors(i):
	start = 1
	divisors = []
	while start <= (i // 2):
		if i % start == 0:
			divisors.append(start)
		start = start + 1
	#print divisors
	return divisors

def solve():
	from common import log

	amicables = []
	total = 0 
	for i in range(1, 10001):
		divisors = get_divisors(i)
		s = sum(divisors)
		# log("%d -- %d " % (i, s))
		if s > i and s<=10000:
			divisors2 = get_divisors(s)
			s2 = sum(divisors2)
			if s2 == i:
				amicables.append((i, s))
				log("%d, %d" % (i, s))
				total = total + i + s

	return total
