# -*- coding: utf-8 -*-

__title__ = "Anagramic squares"

def solve():
    from common import log
    from math import sqrt

    def match(n, p1, p2):
        p1n = list(str(n))
        p2n = list(str(n))

        maps = {}
        for i in range(0, len(p1n)):
            if maps.has_key(p1[i]) and maps[p1[i]] != p1n[i]:
                return False

            maps[p1[i]] = p1n[i]

        for k in maps:
            for j in maps:
                if k != j and maps[k] == maps[j]:
                    return False

        for i in range(0, len(p2n)):
            p2n[i] = maps[p2[i]]
            if p2n[0] == '0':
                return False

        p2n = int("".join(p2n))
        root = int(sqrt(p2n))
        if root*root == p2n:

            log([p1, p2])
            log([n, p2n])

            if p2n > n:
                return p2n
            else:
                return n

        return False

    file = open("data/098.txt", "r")
    data = file.read()
    words = data.split(",")
    words = [(len(word)-2, word[1:-1]) for word in words]

    words.sort()

    pairs = []
    for i in range(0, len(words)-1):
        s = "".join(sorted(list(words[i][1])))
        for j in range(i+1, len(words)):
            if words[j][0] > words[i][0]:
                break
            t = "".join(sorted(list(words[j][1])))
            if s == t:
                log([words[i][1], words[j][1], words[i][0]])
                pairs.append([words[i][1], words[j][1], words[i][0]])

    pairs.reverse()

    limit = int(sqrt(10**9)) + 1
    squares = []
    for i in range(1, limit+1):
        ii = i*i
        diff_number_count = len(set(str(ii)))
        number_count = len(str(ii))
        squares.append([i*i, number_count, diff_number_count])

    squares.reverse()

    for p in pairs:
        for ii, number_count, diff_number_count in squares:
            if number_count > p[2]:
                continue
            if number_count < p[2]:
                break
            if number_count == p[2]:
                matched = match(ii, p[0], p[1])
                if matched:
                    return matched






