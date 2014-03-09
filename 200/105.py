# -*- coding: utf-8 -*-

__title__ = "Special subset sums: testing"

__doc__ = """

Let S(A) represent the sum of elements in set A of size n. 
We shall call it a special sum set if for any two non-empty disjoint 
subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set 
because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} 
satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K 
text file with one-hundred sets containing seven to twelve elements 
(the two examples given above are the first two sets in the file),
identify all the special sum sets, A1, A2, ..., Ak, 
and find the value of S(A1) + S(A2) + ... + S(Ak).

"""

def solve():
	file = open("data/105.txt", "r")
	data = file.read()
	data = data.split("\n")
	grid = []
	for line in data:
		line = line.split(",")
		grid.append([int(n) for n in line])


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

	all_sum = 0
	for items in grid:
		items.sort()
		if verify_rule2(items):
			if verify_rule1(items):
				all_sum = sum(items) + all_sum

	return all_sum





