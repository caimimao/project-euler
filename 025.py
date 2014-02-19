
__title__ = "1000-digit Fibonacci number"

def solve():


	def add(n, m):
		lm = len(m)
		ln = len(n)

		extra = 0
		lmax = max(lm, ln)
		for i in range(0, lmax):
			if i < ln and i < lm:
				tmp = m[i] + n[i] + extra

				extra, m[i] = divmod(tmp, 10)
				#m[i] = tmp % 10
				#extra = tmp / 10

			if (lm>ln) and (i >= ln and i < lm):
				tmp = m[i] + extra
				extra, m[i] = divmod(tmp, 10)
				#m[i] = tmp % 10
				#extra = tmp / 10

			if (ln>lm) and (i >= lm and i < ln):
				tmp = n[i] + extra
				extra, mtemp = divmod(tmp, 10)
				m.append(mtemp)
				#m.append(tmp % 10)
				#extra = tmp /10

		if extra != 0:
			m.append(extra % 10)

		return m

	n = [1]
	m = [1]
	count = 2
	while True:
		m = add(n, m)
		count = count + 1
		if len(m) >= 1000:
			return count

		n = add(m, n)
		count = count + 1
		if len(n) >= 1000:
			return count





