__title__ = "Multiples of 3 and 5"

def solve() :
	from common.math import sum_of_nature
	
	top_number = 1000 - 1
	n3 = (top_number/3)
	#print "n3=%d" % n3
	n5 = (top_number/5)
	#print "n5=%d" % n5
	n15 = (top_number/15)
	#print "n15=%d" % n15

	result = sum_of_nature(n3)*3+sum_of_nature(n5)*5-sum_of_nature(n15)*15
	return result
