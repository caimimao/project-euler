

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





