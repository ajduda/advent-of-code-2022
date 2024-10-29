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



    if a1 <= a2:
        if b1 >= b2:
            ans += 1
            print(f'A: {line}')
            flag = False
    if flag:
        if a2 <= a1:
            if b2 >= b1:
                ans += 1
                print(f'B: {line}')
print(ans)