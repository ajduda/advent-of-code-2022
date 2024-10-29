file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    x = inp.read()
    x = x.strip()

elves = set()

lines = x.split('\n')

for y in range(0,len(lines)):
    for x in range(0,len(lines[y])):
        if lines[y][x] == '#':
            elves.add((x,y))

directions = ['N','S','W','E']

#print(elves)
i = 1
while True:
    triesMoving = set()
    for elf in elves:
        adjacent = -1 # it will count itself
        for dx in range(-1,2):
            for dy in range(-1,2):
                if (elf[0]+dx,elf[1]+dy) in elves:
                    adjacent += 1
        if adjacent > 0:
            triesMoving.add(elf)
    tempElves = elves - triesMoving
    if len(triesMoving) == 0:
        print(i)
        exit()
    movingTo = {}
    blocked = set()
    #print(directions)
    for elf in triesMoving:
        #print(f'elf: {elf}')
        foundLocation = False
        for direction in directions:
            if direction == 'N':
                if (elf[0],elf[1]-1) not in elves and (elf[0]-1,elf[1]-1) not in elves and (elf[0]+1,elf[1]-1) not in elves:
                    if (elf[0],elf[1]-1) in movingTo.values():
                        blocked.add((elf[0],elf[1]-1))
                    movingTo[elf] = (elf[0],elf[1]-1)
                    foundLocation = True
                    #print('elf going NORTH')
                    break
            if direction == 'S':
                if (elf[0],elf[1]+1) not in elves and (elf[0]-1,elf[1]+1) not in elves and (elf[0]+1,elf[1]+1) not in elves:
                    if (elf[0],elf[1]+1) in movingTo.values():
                        blocked.add((elf[0],elf[1]+1))
                    movingTo[elf] = (elf[0],elf[1]+1)
                    foundLocation = True
                    #print('elf going SOUTH')
                    break
            if direction == 'W':
                if (elf[0]-1,elf[1]) not in elves and (elf[0]-1,elf[1]-1) not in elves and (elf[0]-1,elf[1]+1) not in elves:
                    if (elf[0]-1,elf[1]) in movingTo.values():
                        blocked.add((elf[0]-1,elf[1]))
                    movingTo[elf] = (elf[0]-1,elf[1])
                    foundLocation = True
                    #print('elf going EAST')
                    break
            if direction == 'E':
                if (elf[0]+1,elf[1]) not in elves and (elf[0]+1,elf[1]-1) not in elves and (elf[0]+1,elf[1]+1) not in elves:
                    if (elf[0]+1,elf[1]) in movingTo.values():
                        blocked.add((elf[0]+1,elf[1]))
                    movingTo[elf] = (elf[0]+1,elf[1])
                    foundLocation = True
                    #print('elf going WEST')
                    break
        if not foundLocation:
            tempElves.add(elf)
            #print('elf not MOVING')
        #print(f'movingTo: {movingTo}')


    #print(f'BLOCKED: {blocked}')
    for elf in triesMoving:
        #print(elf)
        if elf in tempElves:
            #print('A')
            continue
        if movingTo[elf] in blocked:
            tempElves.add(elf)
            #print('B')
        else:
            tempElves.add(movingTo[elf])
            #print('C')

    directions.append(directions.pop(0))
    elves = tempElves
    i += 1