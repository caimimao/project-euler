
__title__ = "Digit factorials"

def solve():
	from common import log

	def f(n):
		if n == 0 or n == 1:
			return 1
		return reduce(lambda x, y:x*y, range(1, n+1))

	def get_num(a):
		num = []
		t = a
		while True:
			t, m = divmod(t, 10)
			num.append(m)
			if t == 0:
				break

		return num

	fn = map(f, range(0, 10))
	#f(9)*n > 10**n
	def get_max_n():
		n = 2
		f9 = fn[8]
		while f9*n > 10**n:
			n = n + 1
		return n - 1

	n = get_max_n()
	limit = fn[8]*n
	result = 0
	for i in range(10, limit-1):
		num = get_num(i)
		fnum = map(lambda x : fn[x], num)
		if sum(fnum) == i:
			log("%d = %s" % (i, " + ".join(map(lambda x : str(fn[x]), num))))
			result = result + i

	return result

