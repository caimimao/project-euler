
__title__ = "Reciprocal cycles"

def solve():
	from common import log

	def get_dec_repr(d):
		pairs = []
		g = lambda x : str(x[0])

		quit = False
		x = 1
		while not quit:
			pair = divmod(x, d)
			if pair == (0, 0):
				quit = True
				repr = map(g, pairs)
				repr[0] = repr[0] + "."
				log("1/%3d = %s" % (d, "".join(repr)))
				return 0

			if pair in pairs:
				index = pairs.index(pair)

				repr = map(g, pairs)
				repr[0] = repr[0] + "."
				repr.append(")")
				repr[index] = "(" + repr[index]
				log("1/%3d = %s" % (d, "".join(repr)))
				return len(pairs) - index

			pairs.append(pair)
			x = pair[1]*10

	count = [get_dec_repr(i) for i in range(2, 1000)]
	return count.index(max(count)) + 2
		






