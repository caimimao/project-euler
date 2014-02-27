# -*- coding: utf-8 -*-

__title__ = "Anagramic squares"

def solve():
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
                print words[i], words[j]
                pairs.append([words[i], words[j]])

    limit = 10**5
    squres = []




