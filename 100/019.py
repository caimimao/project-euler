
__title__ = "Counting Sundays"

def get_days_from(year):
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		return 366
	else:
		return 365
def get_month_days_from(year):
	data = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if get_days_from(year) == 366:
		data[1] = 29
	return data

def solve():
	
	from common import log
	last_year = 2001
	index = 1 # 1 Jan 1900 was a Monday.		
	count_of_sunday = 0
	for year in range(1901, last_year):
		index = (get_days_from(year-1) + index) % 7

		if index == 0:
			count_of_sunday = count_of_sunday + 1
			
		months = get_month_days_from(year)

		day12 = [index]
		for i in range(0, 11):
			next = (day12[-1] + months[i]) % 7
			day12.append(next)
			if next == 0:
				count_of_sunday = count_of_sunday + 1
		log("%d-%s" %(year, day12))
	return count_of_sunday



