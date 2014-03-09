__title__ = "Lattice paths"

# Answer is C_40^20

def combination(n, m):
	return factorial(n)/(factorial(m)*factorial(n-m))

def factorial(n):
	if n == 1 or n == 0 :
		return 1
	return n*factorial(n-1)

def solve():
	return combination(40, 20)
