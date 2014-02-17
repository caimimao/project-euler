from common import print_head, print_result

print_head(6, title="Sum square difference")

def sum_squares(n):
	return n*(n+1)*(2*n+1)/6

def square_of_sum(n):
	return n*n*(n+1)*(n+1)/4

diff = square_of_sum(100) - sum_squares(100)

print_result(diff)