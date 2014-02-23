
__title__ = ""


def solve():
	from common.util import get_prime_below_seive, isprime

	limit = 100000
	seive = get_prime_below_seive(limit)

	def is_a_prime(n):
		if n >= limit:
			return isprime(n)
		else:
			return seive[n] != 0

	def get_next_perm(perm):
		l = len(perm)
		yield perm
		next = True
		while next:
			min_index = -1
			next = False
			for i in range(l-2, -1, -1):
				if perm[i] > perm[i+1]:

					j = i+1
					for k in range(i+2, l):
						if perm[k] > perm[j] and perm[k] < perm[i]:
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

	for i in range(9, 4, -1):
		n = [str(a) for a in range(i, 0, -1)]
		for next in get_next_perm(n):
			s = "".join(next)
			if is_a_prime(int(s)):
				return s

