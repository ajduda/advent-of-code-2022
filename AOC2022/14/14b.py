with open("input.txt") as inp:
    z = inp.read()
    z = z.strip()

blocked = set()

source = (500,0)

miny = 0  # it's more like max since it's falling towards the positive direction, bad name

for line in z.split('\n'):
    coords = line.split(' -> ')
    for i in range(0,len(coords)-1):
        x1,y1 = coords[i].split(',')
        x2,y2 = coords[i+1].split(',')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        smallery = y1 if y1 > y2 else y2
        if smallery > miny:
            miny = smallery


        if x1 == x2:
            dy = 1 if y1 < y2 else -1
            for n in range(y1,y2+dy,dy):
                blocked.add((x1,n))
        else:
            dx = 1 if x1 < x2 else -1
            for n in range(x1,x2+dx,dx):
                blocked.add((n,y1))


blockedRef = len(blocked)
#print(smallery)
# do sand

sandEscapes = True

miny += 1

#print(blocked)

while (500,0) not in blocked:
    sandx = 500
    sandy = 0
    while True:
        #print(f'({sandx},{sandy})')
        if sandy == miny:
            blocked.add((sandx,sandy))
            break
        elif (sandx,sandy+1) not in blocked:
            sandy += 1
        elif (sandx-1,sandy+1) not in blocked:
            sandx -= 1
            sandy += 1
        elif (sandx+1,sandy+1) not in blocked:
            sandx += 1
            sandy += 1
        else:
            blocked.add((sandx,sandy))
            break



print(len(blocked) - blockedRef)