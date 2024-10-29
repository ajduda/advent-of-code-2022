with open("input.txt") as inp:
    i = inp.read()
    i = i.strip()

maximum = 0
for l in i.split("\n\n"):
    a = 0
    for x in l.split("\n"):
        a += int(x)
    if a > maximum:
        maximum = a

print(maximum)
