
__title__ = "Permuted multiples"

def solve():

	def test(x, n, l):
		y = n*x
		ll = list(str(y))
		ll.sort()
		return ll == l

	i = 11

	while True:
		s = str(i)
		if s[0] != '1' or int(s[1]) > 6:
			i = i + 1

		l = list(str(i))
		l.sort()

		x2 = i*2 

		if test(i, 2, l):
			if test(i, 3, l):
				if test(i, 4, l):
					if test(i, 5, l):
						if test(i, 6, l):
							return i
		i = i + 1
	

