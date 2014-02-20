# -*- coding: utf-8 -*-
__title__ = "Pentagon numbers"

def solve():
	
	from common import log
	from math import sqrt

	def pent(n):
		return n*(3*n-1)/2

	# w = n*(3*n−1)/2
	# (6n-1)(6n-1) = 24*w - 1
	pents = map(pent, range(0, 3000))

	def is_pent(n):
		m = 24*n + 1
		m_root = int(sqrt(m))
		if m_root*m_root == m:
			if (m_root + 1) % 6 == 0 :
				return True
		return False

	def is_pent2(x):
		f = (.5 + sqrt(.25+6*x))/3
		if f - int(f) == 0:
			return True
		else:
			return False

	
	flag = False
	for i in range(1,3000):
		for j in range(i+1,3000):
			if is_pent(pents[j] - pents[i]) and is_pent(pents[j] + pents[i]):
				log("%s - %s" % ([i, j], [pents[i], pents[j]]))
				flag = True
				return (pents[j] - pents[i])
				break
		if flag:
			break	