
__title__ = "Power digit sum"

def solve():
	from common import log
	number = [1]
	p = 1000
	for count in range(0, p):
		extra = 0
		l = len(number)
		for i in range(0, l):
			temp = number[i]*2 + extra
			number[i] = temp % 10
			extra = temp / 10
		if extra > 0:
			number.append(extra)

	number.reverse()
	number_str = map(lambda x: str(x), number)
	log("2**1000=%s" % "".join(number_str))

	return sum(number)
