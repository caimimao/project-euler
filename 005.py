__title__ ="Smallest multiple"

from common.util import gcd, lcm

def solve():
	limit = 21
	number = 1
	for i in range(2, limit):
		number = lcm(number, i)
	return number

