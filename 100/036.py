
__title__ = "Double-base palindromes"

def solve():
	from common import log

	result = []
	def get_repr2(n):
		r = []
		while n>0:
			n, m = divmod(n, 2)
			r.insert(0, str(m))
		return r

	def test2(n):
		r1 = get_repr2(n)
		r2 = list(r1)
		r2.reverse()
		if "".join(r1) == "".join(r2):
			result.append(n)
			log("%8d - %s" % (n, "".join(r1)))
			return True

		return False

	for i in range(1, 10):
		test2(i)        # 1-9
		test2(i*10+i)   # 11-99
	
	
	for i in range(10, 100):
		#ab
		a, b = divmod(i, 10)
		test2(i*10+a) ## 101-999
		test2(i*100+b*10+a) # 1001-9999

	# 10001-99999
	# 100001-999999
	for i in range(100, 999):
		#abc
		a, b = divmod(i, 100)
		b, c = divmod(b, 10)
		test2( i*100 + b*10 + a)
		test2( i*1000 + c*100 + b*10 + a)

	return sum(result)

	