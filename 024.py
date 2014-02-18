__title__ = "Lexicographic permutations"

def solve():
	from common import log

	def get_perms(nums):

		l = len(nums)
		if l == 1:
			return [nums[0]]
		elif l == 2:
			return [nums[0]+nums[1], nums[1]+nums[0]]
		elif l == 3:
			a,b,c = nums
			return [a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a]
		else:
			perms = []
			for i in range(0, l):
				temp_perms = get_perms(nums[0:i] + nums[i+1:])
				for temp in temp_perms:
					perms.append(nums[i] + temp)
			return perms

	string = ['0','1','2','3','4','5','6','7','8','9']
	perms = get_perms(['0','1','2','3','4','5','6','7','8', '9'])
	#print perms
	return perms[999999]




