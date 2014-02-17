from common import print_head, print_result
print_head(9, title="Special Pythagorean triplet")

# a*a + b*b = c*c
# a + b + c = 1000
# ==> a**2 + b**2 = (1000 - a - b)**2 == 1000**2 + (a+b)**2 - 2000*(a+b)
# ==> 1000*(a+b) = 1000*500 + a*b

found = False
for a in range(1, 1000):
	for b in range(1, 1000):
		if 1000*a + 1000*b - a*b == 500000:
			found = True
			print "a=%d, b=%d, c=%d" % (a, b, 1000-a-b)
			print_result(a*b*(1000-a-b))
		if found:
			break
	if found:
		break
