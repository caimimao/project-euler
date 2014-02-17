from common import print_head, print_result
print_head(14, title="Longest Collatz sequence")

def length_of_sequence(number):
	count = 1
	start = number
	while start != 1:
		if start % 2 == 0:
			start = start /2
		else:
			start = 3*start + 1
		count = count + 1
	return count

limit = 1000000

test_number = 2
max_length = 0
max_length_start_number = 0
while test_number< limit:
	length = length_of_sequence(test_number)

	#print "num: %d , length: %d" % (test_number, length)
	if length>max_length:
		max_length_start_number = test_number
		max_length = length
		print "num: %d , length: %d" % (test_number, length)

	test_number = test_number + 1

print_result(max_length_start_number)
