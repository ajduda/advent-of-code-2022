with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

last3 = [x[0],x[1],x[2]]
i = 3
for c in x[3:]:
    #print(last3)
    if c not in last3 and len(set(last3)) == 3:
        print(i+1)
        break
    else:
        i += 1
        last3.pop(0)
        last3.append(c)
