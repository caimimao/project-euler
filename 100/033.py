
__title__ = "Digit canceling fractions"

def solve():
	from common import log
	from common.util import gcd

	px = 1
	py = 1
	for x in range(10, 100):
		for y in range(x+1, 100):
			a, b = divmod(x, 10)
			c, d = divmod(y, 10)

			if b == c and a*y==x*d:
				log([x, y])
				g = gcd(x, y)
				px = px * x /g
				py = py * y /g


	return py/gcd(px, py)


