
__title__ = "Digit fifth powers"

def solve():

	from common import log
	m95 = 9**5

	def find_n():
		n = 1
		while m95*n > 10**(n-1) -1 :
			n = n + 1
		return n - 1

	n = find_n() # n=5

	log("The max length of number is: %d" % n)

	limit = m95*n
	found = []
	hashmap = [i**5 for i in range(0, 10)]
	for i in range(10, limit):
		s = 0 
		test = i
		while True:
			d, m = divmod(test, 10)
			s = s + hashmap[m]
			if d == 0 or s > i:
				break
			test = d
		if s == i:
			log(i)
			found.append(i)

	return sum(found)