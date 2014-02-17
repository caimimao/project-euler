from common import print_head, print_result

print_head(7, title="10001st prime")

from common.math import get_prime_list

primes = get_prime_list(10001)
print primes
print_result(primes[-1])