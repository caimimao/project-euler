
__title__ = "Coded triangle numbers"

def solve():

	from math import sqrt
	from common import log	

	file = open("data/042.txt", "r")
	data = file.read()
	words = data.split(",")


	start_index = ord('A') - 1
	def get_word_number(word):
		s = 0
		for i in word:
			if i != '"':
				s = s + (ord(i) - start_index)
		return s

	# w = 1/2*n*(n+1)  ==> 8w+1 = (2n+1)(2n+1)

	from math import sqrt
	count = 0
	for word in words:
		w = get_word_number(word)
		
		a = int(sqrt(8*w + 1))

		if a*a == 8*w + 1:
			count = count + 1
	return count

