
__title__ = "Triangular, pentagonal, and hexagonal"

def solve():
	from common import log
	
	def t(n):
		return n*(n+1)/2

	def p(n):
		return n*(3*n-1)/2

	def h(n):
		return n*(2*n-1)

	n1 = 285
	n2 = 165
	n3 = 143
	pp = p(n2)
	hh = h(n3)
	while True:
		n1 = n1 + 1
		tt = t(n1)
		while pp<tt:
			n2 = n2 + 1
			pp = p(n2)

		if pp == tt:
			log( "t(%d)=%d" % (n1, tt))
			while hh<tt:
				n3 = n3 + 1
				hh = h(n3)

			if hh == tt:
				log( "t(%d)=%d" % (n1, tt))
				log( "p(%d)=%d" % (n2, pp))
				log( "h(%d)=%d" % (n3, hh))
				return tt




