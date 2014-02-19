

group_size = 5
group_number = 10**5

class BigInt:
	def __init__(self, str):
		self.int_array = []
		l = len(str)
		g = l / group_size
		m = l % group_size

		for i in range(0, g):
			num = str[(l-group_size*i-group_size):(l-group_size*i)]
			self.int_array.append(int(num))

		if m>0:
			num = str[0:m]
			self.int_array.append(int(num))

	def __str__(self):
		s = ""
		for i in self.int_array:
			s = str(i) + s
		return s

	def clone(self):
		c = BigInt("")
		c.int_array = list(self.int_array)

	def len(self):
		return len(self.int_array)

	def add(self, obj):
		l1 = len(self.int_array)
		l2 = len(obj.int_array)

		extra_number = 0
		for i in range(0, max(l1, l2)):
			if i < l1 and i < l2:
				temp = obj.int_array[i] + self.int_array[i] + extra_number
				self.int_array[i] = temp % group_number
				extra_number = temp / group_number

			if i >= l1 and i < l2:
				temp = obj.int_array[i] + extra_number
				self.int_array.append(temp % group_number)
				extra_number = temp / group_number

			if i < l1 and i >= l2:
				temp = self.int_array[i] + extra_number
				self.int_array[i] = temp % group_number
				extra_number = temp / group_number

		if extra_number != 0:
			self.int_array.append(extra_number % group_number)
