

__title__ = ""

def solve():
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	coins = [200, 100, 50, 20, 10, 5, 2, 1]
	l = len(coins)

	count = 1
	p = 200

	def get_comb(p, r):
		#print (p, coins[r:l], "--------")
		if p == 1 or r+1 == l:
			#print (p, coins[r:l], "========== 1")
			return 1

		test = p
		s = 0
		coin = coins[r]
		num = get_comb(test, r+1)
		s = s + num
		while test >= coin:
			test = test - coin
			if test == 0:
				s = s + 1
			else:
				num = get_comb(test, r+1)
				s = s + num
		
		#print (p, coins[r:l], "========== %d" % s)		
		return s

	return get_comb(200, 0)
