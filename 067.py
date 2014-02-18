
__title__ = "Maximum path sum II"

def solve():
	from common import log
	file = open("data/067.txt", "r")
	data = file.read()
	data = data.split("\n")

	grid = []
	for line in data:
		grid.append([int(i) for i in line.split(" ")])

	level = len(grid)
	for y in range(level-2, -1, -1):
		for x in range(0, len(grid[y])):
			grid[y][x] = grid[y][x] + max(grid[y+1][x], grid[y+1][x+1])

	return grid[0][0]