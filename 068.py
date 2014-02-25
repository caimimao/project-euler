# -*- coding: utf-8 -*-

__title__ = "Magic 5-gon ring"

def solve():
	from common import log

	def get_next_perm(perm, l):
		yield perm
		next = True
		while next:
			min_index = -1
			next = False
			for i in range(l-2, -1, -1):
				if perm[i]>perm[i+1]:

					j = i+1
					for k in range(i+2, l):
						if perm[k]>perm[j] and perm[k]<perm[i]:
							j = k

					temp = perm[j]
					perm[j] = perm[i]
					perm[i] = temp

					b = perm[i+1:]
					b.reverse()
					perm[i+1:]=b
					next = True
					break
			yield perm

	
	def test(v):
		# outter-loop 0 1 2 3 4
		# inner-loop 5 6 7 8 9
		# 0, 5, 6
		# 1, 6, 7
		# 2, 7, 8
		# 3, 8, 9
		# 4, 9, 5
		# 056167278389495

		# 10 should stay in the outter loop
		for i in range(5, 10):
			if v[i] == 10:
				return False

		# v[0] should be the minmum of outter-loop
		for i in range(1, 5):
			if v[i] < v[0]:
				return False

		# 
		s = v[4] + v[9] + v[5]
		for i in range(0, 4):
			if (v[i] + v[i+5] + v[i+6]) != s:
				return False
		return True

	def get_number(v):
		s = ""
		o = []
		for i in range(0, 4):
			s = s + (str(v[i]) + str(v[i+5]) + str(v[i+6]))
			o.append((str(v[i]) , str(v[i+5]) , str(v[i+6])))

		s = s + (str(v[4]) + str(v[9]) + str(v[5]))
		o.append((str(v[4]) , str(v[9]) , str(v[5])))
		log(o)
		return int(s)

	s = None
	find_perm = None

	for perm1 in get_next_perm(range(10,5,-1), 5):
		for perm2 in get_next_perm(range(5,0,-1), 5):
			perm = perm1 + perm2
			if test(perm):
				s1 = get_number(perm)
				if not s:
					s = s1
					find_perm = list(perm)
				else:
					if s1 > s:
						s = s1
						find_perm = perm

	return s
