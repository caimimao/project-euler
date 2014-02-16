from common import print_head, print_result

print_head(2)

result = 0

bignum = 600851475143

from common.math import find_one_factor, isprime

all_factors = []

def findall(number):
	print "number=%d" % number
	a = find_one_factor(number)
	if a != 0:
		if isprime(a):
			print a
			all_factors.append(a)
		else:
			findall(a)

		while a != 0 and number>0:
			number = number / a
			print "number=%d" % number
			a = find_one_factor(number)
			if a == 0:
				print number
				all_factors.append(number)
				return
			else:
				if isprime(a):
					print a
					all_factors.append(a)
				else:
					b = a
					findall(b)

findall(bignum)
all_factors.sort()

print_result(all_factors[len(all_factors)-1])