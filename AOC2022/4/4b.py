with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

ans = 0

for line in x.split("\n"):
    l,r = line.split(',')
    a1,b1 = l.split('-')
    a2,b2 = r.split('-')
    flag = True

    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    s1 = set()
    s2 = set()

    for i in range(a1,b1+1):
        s1.add(i)

    for i in range(a2,b2+1):
        s2.add(i)

    if a2 in s1 or b2 in s1:
        ans += 1
    elif a1 in s2 or b2 in s1:
        ans += 1

print(ans)