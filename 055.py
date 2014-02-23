# -*- coding: utf-8 -*-

__title__ = "Lychrel numbers"

def solve():
	pass

	def num2arr(n):
		arr = []
		while n>0:
			d, m = divmod(n, 10)
			arr.append(m)
			n = d
		return arr

	def is_palindromic_number(arr):
		length = len(arr)
		middle = len(arr)/2
		for i in range(0, middle+1):
			if arr[i] != arr[length-i-1] :
				return False
		return True

	def add(arr1, arr2):
		length = len(arr1)
		extra = 0
		for i in range(0, length):
			tmp = arr2[i] + arr1[i] + extra
			extra, arr1[i] = divmod(tmp, 10)

		if extra>0:
			arr1.append(extra)
		return arr1

	def is_lychrel_number(n):
		arr2 = num2arr(n)
		arr1 = list(arr2)
		arr1.reverse()

		count = 0
		while True:

			arrsum = add(arr1, arr2)

			count = count + 1
			if is_palindromic_number(arrsum):
				return False
			else:
				arr1 = arrsum
				arr2 = list(arr1)
				arr2.reverse()
			if count > 50:
				return True

	result = 0
	for x in range(1, 10000):
		if is_lychrel_number(x):
			result = result + 1

	return result








