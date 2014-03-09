# -*- coding: utf-8 -*-

__title__ = "Su Doku"

def solve():

    from common import log
    file = open("data/096.txt", "r")
    data = file.read()
    data = data.split("\n")

    panels = []
    panel = None
    for i in range(0, len(data)):
        if i % 10 == 0:
            if panel:
                panels.append(panel)

            panel = []
        else:
            panel.append([int(x) for x in list(data[i])])

    panels.append(panel)


    def print_panel(p):
        log("")
        log(" ------- ------- ------- ")
        for i in range(0, 9):
            line = p[i]
            log("| %d %d %d | %d %d %d | %d %d %d |" % tuple(line))
            if i == 2 or i == 5 or i == 8:
                log(" ------- ------- ------- ")
        log("")

    #print_panel(panels[0])

    def get_same_block(p, i, j):
        i0 = 3* (i // 3)
        j0 = 3* (j // 3)

        d = []
        for x in range(0, 3):
            for y in range(0, 3):
                x1 = i0 + x
                y1 = j0 + y
                if (x1 != i) or (y1 != j):
                    d.append(p[x1][y1])
        return set(filter(None, d))

    def get_h_line(p, i, j):
        d = []
        for y in range(0, 9):
            if y != j:
                d.append(p[i][y])
        return set(filter(None, d))

    def get_v_line(p, i, j):
        d = []
        for x in range(0, 9):
            if x != i:
                d.append(p[x][j])
        return set(filter(None, d))

    def test_same_block(grid, i, j):
        a = set(grid[i][j])
        i0 = 3* (i // 3)
        j0 = 3* (j // 3)

        for x in range(0, 3):
            for y in range(0, 3):
                x1 = i0 + x
                y1 = j0 + y
                if (x1 != i) or (y1 != j):
                    if grid[x1][y1] != True:
                        a = a - grid[x1][y1]

        if len(a) == 1:
            grid[i][j] = a

    def test_h_line(grid, i, j):
        a = set(grid[i][j])
        d = []
        for y in range(0, 9):
            if y != j:
                if grid[i][y] != True:
                    a = a - grid[i][y]
        if len(a) == 1:
            grid[i][j] = a

    def test_v_line(grid, i, j):
        a = set(grid[i][j])
        d = []
        for x in range(0, 9):
            if x != i:
                if grid[x][j] != True:
                    a = a - grid[x][j]
        if len(a) == 1:
            grid[i][j] = a

    def get_digits(p, i, j):
        if p[i][j] != 0:
            return True
        digits = set(range(1,10))
        #Rules1 - same block
        d1 = get_same_block(p, i, j)
        digits = digits - d1

        #Rule2 - h line
        d2 = get_h_line(p, i, j)
        digits = digits - d2

        #Rule3 - v line
        d3 = get_v_line(p, i, j)
        digits = digits - d3

        return digits

    def done(p):
        for x in range(0, 9):
            for y in range(0, 9):
                if p[x][y] == 0:
                    return False
        return True

    def check(p):
        for x in range(0, 9):
            if sum(p[x]) != 45:
                return False
        for y in range(0, 9):
            s = 0
            for x in range(0, 9):
                s = s + p[x][y]
            if s != 45:
                return False

        s = [0]*81
        for x in range(0, 9):
            for y in range(0, 9):
                i = 3* (x // 3)
                j = 3* (y // 3)
                s[i*3+j] = s[i*3+j] + p[x][y]
        s = filter(None, s)
        if s.count(45) != 9:
            return False
        return True


    def clone_panel(p):
        q = []
        for line in p:
            q.append(list(line))
        return q

    def try_solve(p, loop=0):
        if loop>1:
            return False, p
        p = clone_panel(p)
        update = True
        count = 0
        while update:
            count = count + 1
            update = False
            digits_grid = [[True]*9 for i in range(0, 10)]
            for x in range(0, 9):
                for y in range(0, 9):
                    digits_grid[x][y] = get_digits(p, x, y)
                    if digits_grid[x][y] != True:
                        if len(digits_grid[x][y]) == 0:
                            return False, p

            for x in range(0, 9):
                for y in range(0, 9):
                    if digits_grid[x][y] != True:
                        test_same_block(digits_grid, x, y)
                        test_h_line(digits_grid, x, y)
                        test_v_line(digits_grid, x, y)

            for x in range(0, 9):
                for y in range(0, 9):
                    if digits_grid[x][y] != True:
                        if len(digits_grid[x][y]) == 0:
                            return False, p

                        if len(digits_grid[x][y]) == 1:
                            update = True
                            update_d = list(digits_grid[x][y])[0]
                            p[x][y] = update_d

        if done(p):
            if not check(p):
                return False, p
            return True, p
        else:
            # Guess and Test
            digits_grid = [[True]*9 for i in range(0, 10)]
            for x in range(0, 9):
                for y in range(0, 9):
                    digits_grid[x][y] = get_digits(p, x, y)

            #Try all guess
            for x in range(0, 9):
                for y in range(0, 9):
                    if digits_grid[x][y] != True:
                        if len(digits_grid[x][y])>1:
                            for i in digits_grid[x][y]:
                                p[x][y] = i
                                ok, q = try_solve(p, loop+1)
                                if ok:
                                    return True, q
                                p[x][y] = 0

            return False, p

    count = 0
    s = 0
    for i in range(0, 50):
        found, p = try_solve(panels[i])
        if found:
            count = count + 1
            s = s + (p[0][0]*100+p[0][1]*10+p[0][2])
            #print_panel(p)
            #check(p)
        checked = check(p)
        log([i, found, checked])
        if checked != True:
            print_panel(p)

    return s













