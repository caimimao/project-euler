__title__ = "Even Fibonacci numbers"

def solve() :
	result = 0
	number_limit = 4000000

	a = 1
	b = 2
	result = result + 2
	c = a + b

	while c < number_limit:
		if c % 2 == 0:
			result = result + c
		a = b
		b = c
		c = a + b
	return result

