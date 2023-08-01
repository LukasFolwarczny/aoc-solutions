# https://adventofcode.com/2020/day/4

import sys

L = []

record = {}

for line in sys.stdin:
    if line.strip() == "":
        L.append(record)
        record = {}
    else:
        for l in line.split():
            a,b = l.split(':')
            record[a] = b

L.append(record)

count = 0
count2 = 0

for r in L:
    if len(r.keys()) == 8 or (len(r.keys()) == 7 and 'cid' not in r.keys()):
        count += 1
        good = True
        if not r["byr"].isnumeric() or not 1920 <= int(r["byr"]) <= 2002:
            good = False
        if not r["iyr"].isnumeric() or not 2010 <= int(r["iyr"]) <= 2020:
            good = False
        if not r["eyr"].isnumeric() or not 2020 <= int(r["eyr"]) <= 2030:
            good = False
        height = r['hgt'][:-2]
        if not ((r['hgt'][-2:] == "cm" and height.isnumeric() and 150 <= int(height) <= 193) or (r['hgt'][-2:] == "in" and height.isnumeric() and 59 <= int(height) <= 76)):
            good = False
        if len(r['hcl']) != 7 or r['hcl'][0] != '#':
            good = False
        for i in range(6):
            if len(r['hcl']) == 7 and r['hcl'][i+1] not in list("0123456789abcdef"):
                good = False
        if r['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            good = False
        if len(r['pid']) != 9 or not r['pid'].isnumeric():
            good = False
        if good:
            count2 += 1

print("Part 1")
print(count)
print("Part 2")
print(count2)