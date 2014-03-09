__title__ = "Lexicographic permutations"

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

	count = 0
	for perm in get_next_perm(['0','1','2','3','4','5','6','7','8', '9']):
		count = count + 1
		if count>999999:
			return "".join(perm)




