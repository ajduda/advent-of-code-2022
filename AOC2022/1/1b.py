with open("input.txt") as inp:
    i = inp.read()
    i = i.strip()

amounts = []
for l in i.split("\n\n"):
    a = 0
    for x in l.split("\n"):
        a += int(x)
    amounts.append(a)

amounts.sort()
print(amounts)
print (sum(amounts[-3:]))