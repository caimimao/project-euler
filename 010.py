from common import print_head, print_result
print_head(10, title="Summation of primes")

from common.math import get_prime_below

def sum_of_list(numbers):
	sum = 0
	for i in numbers:
		sum = sum + i
	return sum

primes = get_prime_below(10)
print sum_of_list(primes)

primes = get_prime_below(2000000)
print sum_of_list(primes)


print_result(sum_of_list(primes))
