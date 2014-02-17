from common import print_head, print_result

print_head(5, title="Smallest multiple")

from common.math import gcd, lcm

limit = 21
number = 1
for i in range(2, limit):
	number = lcm(number, i)

print_result(number)