# https://adventofcode.com/2021/day/8

import sys

result = 0

digits = [ "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg" ]

for l in sys.stdin:
    t = {}
    la = l.split("|")[0].strip().split(" ")
    la.sort(key=len)
    s2 = set(la[0])
    s3 = set(la[1])
    s4 = set(la[2])
    s5a = set(la[3])
    s5b = set(la[4])
    s5c = set(la[5])
    s6a = set(la[6])
    s6b = set(la[7])
    s6c = set(la[8])
    s7 = set(la[9])
    t["f"] = (s2 & s3 & s6a & s6b & s6c).pop()
    t["c"] = (s2 - ({t["f"]})).pop()
    t["a"] = (s3 - s2).pop()
    s6all = s6a & s6b & s6c
    s5all = s5a & s5b & s5c
    t["g"] = ((s5all & s6all) - {t["a"]}).pop()
    safg = {t["a"], t["f"], t["g"]}
    t["b"] = (s6all - safg).pop()
    sag = {t["a"], t["g"]}
    t["d"] = (s5all - sag).pop()
    t["e"] = (s7 - {t["a"], t["b"], t["c"], t["d"], t["d"], t["f"], t["g"]}).pop()

    tinv = {}

    for x in t.keys():
        tinv[t[x]] = x
    
    val = 0
    lx = l.strip().split("|")[1].split(" ")
    for x in lx:
        if x == "": continue
        ms = { tinv[a] for a in x }
        y = -1
        for i, dig in enumerate(digits):
            if set(dig) == ms:
                y = i
        val = 10*val + y
    result += val

print("Part 2")
print(result)