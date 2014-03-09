# -*- coding: utf-8 -*-

__title__ = "Special subset sums: optimum"

__doc__ = """
Let S(A) represent the sum of elements in set A of size n. 
We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, 
the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. 

The first five optimum special sum sets are given below.
n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, 
the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, 
where b is the "middle" element on the previous row.
By applying this "rule" we would expect the optimum set 
for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. 
However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. 
The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115
 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to problems 105 and 106.
"""

def solve():
	from common import log

	def verify_rule1(items):
		result = {}
		l = len(items)
		for bitpos in range(1, 2**l):
			s = 0
			for i in range(0, l):
				if bitpos & 1 == 1:
					s = s + items[i]
				bitpos = bitpos >> 1
			if result.has_key(s):
				return False
			else:
				result[s] = 1
		return True

	def verify_rule2(items):
		# if a1<a2<...<an
		# a1+a2>a(n)  => a(x)+a(y)>a(1)+a(2)>a(n)>a(z)
		# a1+a2+a3>a(n)+a(n-1)
		# ...
		s1 = items[0]
		s2 = 0
		l = len(items)
		for i in range(0, l/2):
			s1 = s1 + items[i+1]
			s2 = s2 + items[l-i-1]
			if (s1 <= s2):
				return False
		return True

	n6 = [11, 18, 19, 20, 22, 25]
	n7 = [20] + [x + 20 for x in n6]

	limit = sum(n7) + 1
	for x1 in range(0, limit):
 		for x2 in range(x1 + 1, limit - x1):
  			for x3 in range(x2 + 1, min(limit - x1 - x2, x1 + x2)):
   				for x4 in range(x3 + 1, min(limit - x1 - x2 - x3, x1 + x2)):
					for x5 in range(x4 + 1, min(limit - x1 - x2 - x3 - x4, x1 + x2)):
						for x6 in range(x5 + 1, min(limit - x1 - x2 - x3 - x4 - x5, x1 + x2)):
							for x7 in range(x6 + 1, min(limit - x1 - x2 - x3 - x4 - x5 - x6, x1 + x2)):
								ls = [x1, x2, x3, x4, x5, x6, x7]
								if verify_rule2(ls) and verify_rule1(ls):
									log(sum(ls))
									return "".join([str(x) for x in ls])






