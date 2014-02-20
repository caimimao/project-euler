
__title__ = "Sub-string divisibility"

def solve():
	from common import log
	def get_next_perm(perm):
		l = len(perm)
		yield perm
		next = True
		while next:
			min_index = -1
			next = False
			for i in range(l-2, -1, -1):
				if perm[i]<perm[i+1]:

					j = i+1
					for k in range(i+2, l):
						if perm[k]<perm[j] and perm[k]>perm[i]:
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


	perm = [str(a) for a in range(0, 10)]

	def test(n, m):
		return n % m == 0

	p = [1, 2, 3, 5, 7, 11, 13, 17]
	s = 0
	for next in get_next_perm(perm):
		if next[0] != '0':
			found = True
			for i in range(1, 8):
				x = int("".join(next[i:i+3]))
				if x % p[i] != 0:
					found = False
					break
			if found:
				log("".join(next))
				s = s + int("".join(next))
	return s




