
__title__ = "Pandigital products"

def solve():
	from common import log
	def get_num(a):
		num = []
		t = a
		while True:
			t, m = divmod(t, 10)
			num.append(m)
			if t == 0:
				break

		return num

	def test(a, b):
		m = {}
		s = [a, b]
		for n in s:
			num = get_num(n)
			for i in num:
				if m.has_key(i) or i == 0:
					return False
				m[i] = 1
		num = get_num(a*b)
		for i in num:
			if m.has_key(i) or i == 0:
				return False
			m[i] = 1

		if len(m) == 9:
			return True
		return False

	result = []
	for x in range(1, 10):
		for y in range(1000, 10000):
			if test(x, y):
				log([x, y, x*y])
				result.append(x*y)

	for x in range(10, 100):
		for y in range(100, 1000):
			if test(x, y):
				log([x, y, x*y])
				result.append(x*y)

	return sum(set(result))