with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

last13 = [x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12]]
i = 14
for c in x[14:]:
    #print(last14)
    if c not in last13 and len(set(last13)) == 13:
        print(i+1)
        break
    else:
        i += 1
        last13.pop(0)
        last13.append(c)