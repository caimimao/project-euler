
__title__ = "Number spiral diagonals"

def solve():
	#1001x1001 grid has 500 level (ignore level 0)
	#level_0 - 1
	#level_1 - 3, 3+2, 3+4, 3+6  (interval 2*n = 1)
	#level_2 - 13, 13+4, 13+8, 13+12  (interval 2*n = 4)
	#...
	#level_n - A(n), A(n)+2n, A(n)+4n, A(n)+6n (interval 2*n)

	# where A(n) = A(n-1) + 6(n-1) + 2n = A(n-1) + 8n - 6
	# then S(n) = A(n) + A(n)+2n + A(n)+4n + A(n)+6n = 4A(n) + 12n

	s = 1
	a = 1
	for n in range(1, 501):
		a = a + 8*n - 6
		s = s + 4*a + 12*n

	return s

