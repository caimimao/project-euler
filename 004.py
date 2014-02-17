from common import print_head, print_result

print_head(4, title="Largest palindrome product")

def is_palindromic(number):
	single_numbers = []
	num = number
	while number>0:
		single = number % 10
		number = number / 10
		single_numbers.append(single)

	l = len(single_numbers)
	#print num
	#print single_numbers
	for i in range(1, l/2 + 1):
		#print "%s, %s" % (i-1, l-i)
		#print "%s, %s" % (single_numbers[i-1], single_numbers[l-i])
		if single_numbers[i-1] != single_numbers[l-i]:
			return False
	
	return True

result = 0

for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		p = i * j

		if result == 0:
			if is_palindromic(p): 
				result = p
		else:
			if p>result and is_palindromic(p):
				result = p

print_result(result)