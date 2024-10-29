with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

hpos = [0,0]
tpos = [0,0]

tailVisited = {(0,0)}

for line in x.split('\n'):
    #print(f'{hpos} : {tpos}')
    direction,length = line.split(' ')
    length = int(length)
    if direction == 'U':
        for i in range(0,length):
            hpos[1] += 1
            if abs(hpos[1]-tpos[1]) > 1:
                tpos[1] += 1
                if tpos[0] != hpos[0]:
                    tpos[0] = hpos[0]
                tailVisited.add((tpos[0],tpos[1]))
    if direction == 'D':
        for i in range(0,length):
            hpos[1] -= 1
            if abs(hpos[1]-tpos[1]) > 1:
                tpos[1] -= 1
                if tpos[0] != hpos[0]:
                    tpos[0] = hpos[0]
                tailVisited.add((tpos[0],tpos[1]))
    if direction == 'L':
        for i in range(0,length):
            hpos[0] -= 1
            if abs(hpos[0]-tpos[0]) > 1:
                tpos[0] -= 1
                if tpos[1] != hpos[1]:
                    tpos[1] = hpos[1]
                tailVisited.add((tpos[0],tpos[1]))
    if direction == 'R':
        for i in range(0,length):
            hpos[0] += 1
            if abs(hpos[0]-tpos[0]) > 1:
                tpos[0] += 1
                if tpos[1] != hpos[1]:
                    tpos[1] = hpos[1]
                tailVisited.add((tpos[0],tpos[1]))

#print(tailVisited)

print(len(tailVisited))
