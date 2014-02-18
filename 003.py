__title__ = "Largest prime factor"
from common import log

def solve() :
	result = 0
	bignum = 600851475143
	from common.math import find_one_factor, isprime

	all_factors = []

	def findall(number):
		log("number=%d" % number)
		a = find_one_factor(number)
		if a != 0:
			if isprime(a):
				log(a)
				all_factors.append(a)
			else:
				findall(a)

			while a != 0 and number>0:
				number = number / a
				log("number=%d" % number)
				a = find_one_factor(number)
				if a == 0:
					log(number)
					all_factors.append(number)
					return
				else:
					if isprime(a):
						log(a)
						all_factors.append(a)
					else:
						b = a
						findall(b)

	findall(bignum)
	all_factors.sort()
	return all_factors[-1]
