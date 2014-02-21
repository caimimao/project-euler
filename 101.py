

__title__ = "Optimum polynomial"

def solve():
	from common import log
	param = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
	#param = [0, 0, 0, 1]
	def u(n):
		l = len(param)
		s = 0
		nn = 1
		i = 0
		while i < l:
			s = s + nn*param[i]
			i = i + 1
			nn = nn*n
		return s

	def get_next_seq(seq):
		return [seq[i]-seq[i-1] for i in range(1, len(seq))]

	seq = map(u, range(1, len(param)))
	for i in range(1, len(param)):
		log("u(%02d) = %d" % (i, seq[i-1]))
	grid = []
	grid.append(seq)
	log(seq)
	for i in range(0, len(seq)-1):
		grid.append(get_next_seq(grid[i]))
		log(grid[i+1])

	return sum([sum(grid[line]) for line in range(0, len(grid))])

