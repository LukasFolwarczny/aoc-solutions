# https://adventofcode.com/2022/day/11

# For fun also the naive implementation of Part 2.
# It prints the current round.

import sys

l = ""


monkeys = []

class monkey:
    def __init__(self, id, items, fun, divisor, where):
        self.id = id
        self.items = items
        self.fun = fun
        self.divisor = divisor
        self.where = where
        self.inspected = 0

def parsefun(oper):
    s = oper.split()
    op = s[3]
    se = s[4]
    if se == "old":
        if op == "+":
            return lambda a : a * 2
        if op == "*":
            return lambda a : a ** 2
    else:
        if op == "+":
            return lambda a : a + int(se)
        if op == "*":
            return lambda a : a * int(se)

itemid = 0

while ((l := sys.stdin.readline())):
    id = int(l.split()[1].split(':')[0])
    items = []
    for i in sys.stdin.readline().split(":")[1].split(","):
        items.append((itemid,int(i)))
        itemid += 1
    fun = parsefun(sys.stdin.readline().split(":")[1])
    divisor = int(sys.stdin.readline().split(":")[1].split()[2])
    where = [0,0]
    where[1] = int(sys.stdin.readline().split(":")[1].split()[3])
    where[0] = int(sys.stdin.readline().split(":")[1].split()[3])
    monkeys.append(monkey(id, items, fun, divisor, where))
    sys.stdin.readline()

for round in range(10000):
    print(round)
    for m in monkeys:
        for i in m.items:
            m.inspected += 1
            wnew = m.fun(i[1])
            #wnew //= 3        
            monkeys[m.where[wnew % m.divisor == 0]].items.append((i[1],wnew))
        m.items = []

insp = sorted(m.inspected for m in monkeys)

print("Part 2")
print(insp[-1]*insp[-2])