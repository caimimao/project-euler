
__title__ = "Non-abundant sums"
from math import sqrt

def get_divisors_sum(i):
	s = 1
	start = 2
	n_root = sqrt(i)
	while start <= n_root:
		if i % start == 0:
			s = s + start + i/start
		start = start + 1
	if n_root == int(n_root):
		s = s - n_root
	return s

def solve():
	#print abn(28123)
	#return 
	from common import log
	limit = 28123
	#limit = 100
	abundants = set()
	s = 0
	for i in range(1, limit+1):
		if get_divisors_sum(i) > i:
			abundants.add(i)
		if not any((i - a in abundants) for a in abundants):
			s = s + i
	#log("abundants count: %d" % len(abundants))

	return s


