with open("input.txt") as inp:
    z = inp.read()
    z = z.strip()

elev = []

y = 0
for line in z.split('\n'):
    x = 0
    elev.append([])
    for c in line:
        if c == 'S':
            elev[-1].append(1)
        elif c == 'E':
            start = (y,x)
            elev[-1].append(26)
        else:
            elev[-1].append(ord(c)-ord('a')+1)
        x += 1
    y += 1

possible = {}

for y in range(0,len(elev)):
    for x in range(0,len(elev[0])):
        possible[(y,x)] = []
        if y > 0:
            if elev[y][x] <= elev[y-1][x] + 1:
                possible[(y,x)].append((y-1,x))
        if y < len(elev) - 1:
            if elev[y][x] <= elev[y+1][x] + 1:
                possible[(y,x)].append((y+1,x))
        if x > 0:
            if elev[y][x] <= elev[y][x-1] + 1:
                possible[(y,x)].append((y,x-1))
        if x < len(elev[0]) - 1:
            if elev[y][x] <= elev[y][x+1] + 1:
                possible[(y,x)].append((y,x+1))

#print(possible)

searched = {start}

i = 0
while len(searched) < len(possible):
    buffer = set()
    for coord in searched:
        for possibility in possible[coord]:
            if possibility not in searched:
                buffer.add(possibility)
    i += 1
    for coord in buffer:
        y,x = coord
        if elev[y][x] == 1:
            print(i)
            exit()
        searched.add(coord)
    

print('error')