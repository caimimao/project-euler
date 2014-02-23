
__title__ = "Combinatoric selections"

def solve():

	from common import log

	def factorial(n):
		if n == 1 or n == 0 :
			return 1
		return n*factorial(n-1)

	fn = map(factorial, range(0, 101));

	def comb(n, m):
		return fn[n]/fn[m]/fn[n-m]

	count = 0
	for n in range(2, 101):
		for r in range(0, n+1):
			temp = comb(n, r)
			if temp > 1000000:
				count = count + 1
	return count
