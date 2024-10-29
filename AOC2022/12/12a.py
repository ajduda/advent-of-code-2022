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
            start = (y,x)
            elev[-1].append(1)
        elif c == 'E':
            end = (y,x)
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
            if elev[y][x] + 1 >= elev[y-1][x]:
                possible[(y,x)].append((y-1,x))
        if y < len(elev) - 1:
            if elev[y][x] + 1 >= elev[y+1][x]:
                possible[(y,x)].append((y+1,x))
        if x > 0:
            if elev[y][x] + 1 >= elev[y][x-1]:
                possible[(y,x)].append((y,x-1))
        if x < len(elev[0]) - 1:
            if elev[y][x] + 1 >= elev[y][x+1]:
                possible[(y,x)].append((y,x+1))


searched = {start}

i = 0
while end not in searched:
    buffer = set()
    for coord in searched:
        for possibility in possible[coord]:
            if possibility not in searched:
                buffer.add(possibility)
    for coord in buffer:
        searched.add(coord)
    i += 1

print(i)