
__title__ = "Poker hands"

def solve():
	file = open("data/054.txt", "r")
	data = file.read()
	data = data.split("\n")

	grid = []
	for line in data:
		line = line.split(" ")
		a = line[0:5]
		b = line[5:10]
		grid.append((a,b))


	# 1 High Card: Highest value card.
	# 2 One Pair: Two cards of the same value.
	# 3 Two Pairs: Two different pairs.
	# 4 Three of a Kind: Three cards of the same value.
	# 5 Straight: All cards are consecutive values.
	# 6 Flush: All cards of the same suit.
	# 7 Full House: Three of a kind and a pair.
	# 8 Four of a Kind: Four cards of the same value.
	# 9 Straight Flush: All cards are consecutive values of same suit.
	#10 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.	

	# 2, 3, 4, 5, 6, 7, 8, 9, 10(T), Jack(J), Queen[Q], King[K], Ace[A].

	order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	order_map = {}
	for i in range(0, len(order)):
		order_map[order[i]] = i + 2

	def get_orders(cards):
		return [order_map[x[0]] for x in cards]

	def is_one_pairs(cards):
		o = get_orders(cards)
		o.sort()
		for i in range(0, 4):
			if o[i] == o[i+1]:
				return True
		return False

	def is_two_pairs(cards):
		o = get_orders(cards)
		o.sort()
		count = 0
		for i in range(0, 4):
			if o[i] == o[i+1]:
				count = count + 1
		if count == 2:
			return True
		return False

	def is_three_kind(cards):
		o = get_orders(cards)
		o.sort()
		if o[0] == o[1] and o[1] == o[2]:
			return True
		if o[1] == o[2] and o[2] == o[3]:
			return True
		if o[2] == o[3] and o[3] == o[4]:
			return True
		return False

	def is_straight(cards):
		orders = get_orders(cards)
		orders.sort()
		for i in range(0, 4):
			if orders[i+1] - orders[i] != 1:
				return False
		return True

	def is_flush(cards):
		for i in range(1, 5):
			if cards[i][1] != cards[0][1]:
				return False
		return True

	def is_full_house(cards):
		o = get_orders(cards)
		o.sort()
		if (o[0] == o[1] and o[1] == o[2]) and (o[3] == o[4]):
			return True
		if (o[0] == o[1]) and (o[2] == o[3] and o[3] == o[4]):
			return True
		return False

	def is_four_kind(cards):
		o = get_orders(cards)
		o.sort()
		if o[0] == o[1] and o[1] == o[2] and o[2] == o[3]:
			return True
		if o[1] == o[2] and o[2] == o[3] and o[3] == o[4]:
			return True
		return False

	def is_straight_flush(cards):
		if is_flush(cards) and is_straight(cards):
			return True
		return False

	def is_royal_flush(cards):
		if is_straight_flush(cards):
			orders = get_orders(cards)
			orders.sort()
			if orders[0] == 10:
				return True
		return False

	def cmp1(a, b):
		oa = get_orders(a)
		oa.sort()
		ob = get_orders(b)
		ob.sort()
		for i in range(4, -1, -1):
			if oa[i] > ob[i]:
				return 1
			if oa[i] < ob[i]:
				return -1
		return 0

	def cmp2(a, b):
		oa = get_orders(a)
		oa.sort()
		ob = get_orders(b)
		ob.sort()

		for i in range(0, 4):
			if oa[i] == oa[i+1]:
				pa = oa[i]
			if ob[i] == ob[i+1]:
				pb = ob[i]

		if pa > pb:
			return 1
		if pa < pb:
			return -1

		for i in range(4, -1, -1):
			if oa[i] > ob[i]:
				return 1
			if oa[i] < ob[i]:
				return -1
		return 0

	def get_level(cards):
		if is_royal_flush(cards):
			return 10
		if is_straight_flush(cards):
			return 9
		if is_four_kind(cards):
			return 8
		if is_full_house(cards):
			return 7
		if is_flush(cards):
			return 6
		if is_straight(cards):
			return 5
		if is_three_kind(cards):
			return 4
		if is_two_pairs(cards):
			return 3
		if is_one_pairs(cards):
			return 2
		return 1

	count = 0
	for card in grid:
		la = get_level(card[0])
		lb = get_level(card[1])
		if la > lb:
			count = count + 1
		if la == lb:
			if la == 1:
				if cmp1(card[0], card[1]) == 1:
					count = count + 1
			if la == 2:
				if cmp2(card[0], card[1]) == 1:
					count = count + 1
	return count

