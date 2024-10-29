file, row = 'test.txt',10
file, row = 'input.txt',2000000

with open(file) as inp:
    z = inp.read()
    z = z.strip()

xbounds = []
ybounds = []

#construct bounds
for line in z.split('\n'):
    _,_,x1,y1,_,_,_,_,x2,y2 = line.split(' ')
    x1 = int(x1[2:-1])
    x2 = int(x2[2:-1])
    y1 = int(y1[2:-1])
    y2 = int(y2[2:])

    if len(xbounds) == 0:
        xbounds.append(min(x1,x2))
        xbounds.append(max(x1,x2))
        ybounds.append(min(y1,y2))
        ybounds.append(max(y1,y2))
    else:
        if min(x1,x2) < xbounds[0]:
            xbounds[0] = min(x1,x2)
        if max(x1,x2) > xbounds[1]:
            xbounds[1] = max(x1,x2)
        if min(y1,y2) < ybounds[0]:
            ybounds[0] = min(y1,y2)
        if min(y1,y2) > ybounds[1]:
            ybounds[1] = max(y1,y2)

print(xbounds)
print(ybounds)

rowList = []
for i in range(0,(xbounds[1]-xbounds[0])*3//2): # This might be overkill
    rowList.append(0)

answerOffset = set()  # beacons in the row

#find answer
for line in z.split('\n'):
    _,_,x1,y1,_,_,_,_,x2,y2 = line.split(' ')
    x1 = int(x1[2:-1])
    x2 = int(x2[2:-1])
    y1 = int(y1[2:-1])
    y2 = int(y2[2:])

    if y2 == row:
        answerOffset.add((x2,y2))
        #print(f'DEBUG: ({x1},{y1}) -> ({x2},{y2})')

    print(f'({x1},{y1}) -> ({x2},{y2})')

    dist = abs(x2-x1) + abs(y2-y1)
    #print(abs(row-y1),dist+1)

    for i in range(0,dist+1-(abs(row-y1))):  # This was shotgun debugging to find this expression
        #print(f'i: {i}')
        rowList[x1+i-xbounds[0]] = 1
        rowList[x1-i-xbounds[0]] = 1

print(sum(rowList)-len(answerOffset))