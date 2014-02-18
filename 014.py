__title__ = "Longest Collatz sequence"




def solve():
	from common import log

	limit = 1000000
	def length_of_sequence(number):
		count = 1
		start = number
		while start != 1:
			if start % 2 == 0:
				start = start >> 1
			else:
				start = start+start+start + 1

			count = count + 1
		return count

	test_number = 2
	max_length = 0
	max_length_start_number = 0
	while test_number< limit:
		length = length_of_sequence(test_number)

		#print "num: %d , length: %d" % (test_number, length)
		if length>max_length:
			max_length_start_number = test_number
			max_length = length
			log("num: %d , length: %d" % (test_number, length))

		test_number = test_number + 1

	return max_length_start_number
