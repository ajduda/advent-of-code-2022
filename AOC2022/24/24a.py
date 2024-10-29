file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

lines = z.split('\n')

# Current idea is to use a modified flood fill approach
blizzards = {'>':[],'<':[],'^':[],'v':[]}
walls = set()
for y in range(0,len(lines)):
    for x in range(0,len(lines[y])):
        if lines[y][x] == '#':
            walls.add((x,y))
        elif lines[y][x] != '.':
            blizzards[lines[y][x]].append([x,y])

walls.add((1,-1))  # so we can't try to go out the way we came

end = (lines[-1].index('.'),len(lines)-1)

directions = {'>':(1,0),'<':(-1,0),'^':(0,-1),'v':(0,1)}

possiblePositions = {(1,0)}
iterations = 0
while end not in possiblePositions:
    blizzardCoords = set()
    for direction in directions:
        (dx,dy) = directions[direction]
        for i in range(0,len(blizzards[direction])):
            blizzard = blizzards[direction][i]
            blizzard[0] += dx
            blizzard[1] += dy
            if (blizzard[0],blizzard[1]) in walls:
                if dx == 1:
                    blizzard[0] = 1
                if dy == 1:
                    blizzard[1] = 1
                if dx == -1:
                    blizzard[0] = len(lines[0])-2
                if dy == -1:
                    blizzard[1] = len(lines)-2
            blizzards[direction][i] = blizzard
            blizzardCoords.add((blizzard[0],blizzard[1]))
    newPositions = set()
    for x,y in possiblePositions:
        newPositions.add((x-1,y))
        newPositions.add((x+1,y))
        newPositions.add((x,y+1))
        newPositions.add((x,y-1))
        newPositions.add((x,y))

    newPositions -= walls
    newPositions -= blizzardCoords

    possiblePositions = newPositions
    #print(possiblePositions)
    iterations += 1

    """print(f'GRID FOR ITERATION {iterations}')
    for y in range(0,len(lines)):
        for x in range(0,len(lines[y])):
            c = ' '
            if (x,y) in walls:
                c = '#'
            elif (x,y) in blizzardCoords:
                c = 'X'
            elif (x,y) in possiblePositions:
                c = '.'
            print(c,end='')
        print()
    print('\n')"""

print(iterations)
