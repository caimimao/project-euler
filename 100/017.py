
__title__ = "Number letter counts"

def get_word(i):
	NUMBER_CONSTANT = {0:"zero ", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",  
		8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",  
		14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen" }

	IN_HUNDRED_CONSTANT = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}  
	BASE_CONSTANT = {0:" ", 1:"hundred", 2:"thousand", 3:"million", 4:"billion"};  	

	if i<20:
		return [NUMBER_CONSTANT[i]]

	if i>=20 and i<100:
		if i % 10 == 0:
			return [IN_HUNDRED_CONSTANT[i//10]]
		else:
			return [IN_HUNDRED_CONSTANT[i//10], NUMBER_CONSTANT[i%10]]

	if i>=100 and i<1000:
		if i % 100 == 0: 
			return [NUMBER_CONSTANT[i//100], BASE_CONSTANT[1]]
		else:
			a = i % 100
			word = [NUMBER_CONSTANT[i//100] , BASE_CONSTANT[1] , "and"]
			word.extend(get_word(a))
			return word
	if i == 1000:
		return [NUMBER_CONSTANT[1] , BASE_CONSTANT[2]]

def solve():
	from common import log
	count = 0
	for i in range(1, 1001):
		word = get_word(i)
		log("%5d - %s" % (i, " ".join(word)))
		count = count + len("".join(word))

	return count




