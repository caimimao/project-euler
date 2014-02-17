

def sum_of_nature(n):
	return n*(n+1)/2

_small_filter = [2, 3, 5, 7, 11, 13, 17]

def find_one_factor(number):
	if number == 1 or number == 2:
		return 0
	if number in _small_filter:
		return 0
	
	for a in _small_filter:
		if number % a == 0:
			return a

	div = 19
	while div < number/2:
		if number % div == 0:
			return div
		div = div + 2
	return 0

def isprime(number):
	factor = find_one_factor(number)
	if factor == 0:
		return True
	else:
		return False

#Greatest Common Divisor
def gcd(a, b):
	if b>a:
		a, b = b, a
	r = a % b

	while r != 0:
		a = b
		b = r
		r = a % b
	return b

#Least Common Multiple
def lcm(a, b):
	return a/gcd(a,b)*b


def get_prime_list(count):
	primes = [2, 3, 5, 7, 11, 13]
	found_count = 6
	test_number = 15
	test_number_div_2 = 8

	while found_count<count:
		is_prime = True
		for i in primes:
			if i<test_number_div_2 and test_number % i == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(test_number)
			found_count = found_count + 1

		test_number = test_number + 2
		test_number_div_2 = test_number_div_2 + 1

	return primes

def get_prime_below(number):
	number_map = {}
	start = 2

	while start<number:
		if not number_map.has_key(start):
			c = number/start
			for i in range(2, c+1):
				number_map[start*i] = False
		start = start + 1

	primes = []
	for i in range(2, number+1):
		if not number_map.has_key(i):
			primes.append(i)
	return primes




