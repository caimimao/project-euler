

__title__ = ""

def solve():
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	coins = [200, 100, 50, 20, 10, 5, 2, 1]
	l = len(coins)

	count = 1
	p = 200

	def get_comb(p, r):

		if p == 1:
			return 1

		test = p
		s = 0
		for i in range(r, l):
			coin = coins[i]
			num = get_comb(test, r+1)
			s = s + num
			while test >= coin:
				test = test - coin
				if test == 0:
					s = s + 1
				else:
					num = get_comb(test - coin, r+1)
					s = s + num
		
		print (p, coins[r:l])		
		return s

	print get_comb(4, 0)
