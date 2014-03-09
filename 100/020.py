__title__ = "Factorial digit sum"

def solve():
	from common import log
	number = [1]

	for x in range(1, 101):
		extra = 0
		l = len(number)
		for i in range(0, l):
			temp = number[i]*x + extra
			number[i] = temp % 10
			extra = temp // 10
		if extra > 0:
			while extra > 0:
				temp = extra % 10
				number.append(temp)
				extra = extra // 10
	number.reverse()
	number_str = map(lambda x: str(x), number)
	log("100!=%s" % "".join(number_str))

	return sum(number)		
