# -*- coding: utf-8 -*-

__title__ = "XOR decryption"

def solve():
    from common import log

    file = open("data/059.txt", "r")
    data = file.read()
    word = data.split(",")
    word = [int(w) for w in word]


    def xor(pwd, text):
        result = []
        i = 0
        for t in text:
            k = pwd[i]
            result.append(k^t)
            i = (i + 1) % 3
        return result

    def test_english(text):
        text = [chr(i) for i in text]
        text = "".join(text)
        text = text.split(" ")
        s = 0
        s = s + text.count("a")
        s = s + text.count("the")
        s = s + text.count("in")
        if s>5:
            return text
        else:
            return False

    b = ord('a')
    c = ord('z')
    for x in range(b, c+1):
        for y in range(b, c+1):
            for z in range(b, c+1):
                pwd = [x, y, z]
                dtext = xor(pwd, word)
                dtext = test_english(dtext) 
                if dtext != False:
                    dtext = " ".join(dtext)
                    log(dtext)
                    s = sum(map(ord, dtext))
                    return s

