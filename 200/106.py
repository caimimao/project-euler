
__title__ = ""

#http://www.mathblog.dk/project-euler-106-minimum-comparisons-special-sum-sets/
def solve():

	# x(n, s) = 1/2 * C(n, 2s) * C(2s, s) - (1/[s+1])* C(2s, s) * C(n, 2s)
	#         = [1/2 - 1/(s+1)] (C(n, 2s) * C(2s, s))
	#         = [(s-1)n!]/[2(s+1)!s!(n-2s)!]

	def choose(n, m):
		s = 1
		for i in range(n-m+1, n+1):
			s = s * i
		for i in range(2, m+1):
			s = s / i
		return s

	result = 0
	n = 12
	for s in range(2, n/2+1):
		a = (choose(n, 2*s)*choose(2*s, s))
		result = result + a/2 - a/(s+1)

	return result