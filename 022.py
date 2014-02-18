__title__ = "Names scores"

def solve():
	from common import log
	file = open("data/022.txt", "r")
	data = file.read()
	names = data.split(",")
	names.sort()

	start_index = ord('A') - 1
	def name_to_number(name):
		s = 0
		for i in name:
			if i != '"':
				s = s + (ord(i) - start_index)
		return s

	line = 1
	total = 0
	for name in names:
		total = total + line* name_to_number(name)
		line = line + 1
	print total
