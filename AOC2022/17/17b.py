file = 'test.txt'
file = 'input.txt'

goal = 1000000000000

iterations = 50000

repeatingIndex = 20

with open(file) as inp:
    z = inp.read()
    z = z.strip()

pattern = z

def getShape(n,y):
    shape = []
    if n == 0:
        shape.append([2,3+y])
        shape.append([3,3+y])
        shape.append([4,3+y])
        shape.append([5,3+y])
    elif n == 1:
        shape.append([3,4+y])
        shape.append([3,5+y])
        shape.append([3,3+y])
        shape.append([2,4+y])
        shape.append([4,4+y])
    elif n == 2:
        shape.append([2,3+y])
        shape.append([3,3+y])
        shape.append([4,3+y])
        shape.append([4,4+y])
        shape.append([4,5+y])
    elif n == 3:
        shape.append([2,3+y])
        shape.append([2,4+y])
        shape.append([2,5+y])
        shape.append([2,6+y])
    elif n == 4:
        shape.append([2,3+y])
        shape.append([3,3+y])
        shape.append([2,4+y])
        shape.append([3,4+y])
    else:
        print('shape error')
        exit()
    return shape


grid = set()
i = 0

maxY = 0
n = 0

for j in range(0,iterations):  # run the simulation out quite a ways first
    #print(f'{n}:{maxY}')
    #if n % 5 == 0:
        #print(f'n:{n}  i:{i}  maxY:{maxY}')
    shape = getShape(n%5,maxY)
    desending = True
    while desending:
        if pattern[i%len(pattern)] == '<':  # left
            canMove = True
            for coord in shape:
                if coord[0] == 0:
                    canMove = False
            if canMove:
                for coord in shape:
                    if (coord[0]-1,coord[1]) in grid:
                        canMove = False
            if canMove:
                for coord in shape:
                    coord[0] -= 1
        else:
            canMove = True
            for coord in shape:
                if coord[0] == 6:
                    canMove = False
            if canMove:
                for coord in shape:
                    if (coord[0]+1,coord[1]) in grid:
                        canMove = False
            if canMove:
                for coord in shape:
                    coord[0] += 1
        i += 1

        canMove = True
        for coord in shape:
            if coord[1] == 0:
                canMove = False
        if canMove:
            for coord in shape:
                if (coord[0],coord[1]-1) in grid:
                    canMove = False

        if canMove:
            for coord in shape:
                coord[1] -= 1
            continue
        else:
            for coord in shape:
                grid.add((coord[0],coord[1]))
                if coord[1]+1 > maxY:
                    maxY = coord[1]+1
            desending = False
            n += 1

print(f'Simulation run to {iterations}')
iSnapshot = i % len(pattern)
nSnapshot = n % 5

# From using the info above, along with code under the exit, I determined that it loops
# for every time n increases 1715, maxY increases by 2616

print(n)
loopingTimes = (goal - iterations) // 1715
remainingTimes = (goal - iterations) % 1715
print(loopingTimes)
print(remainingTimes)

for j in range(0,remainingTimes):  # run the simulation out quite a ways first
    #print(f'{n}:{maxY}')
    #if n % 5 == 0:
        #print(f'n:{n}  i:{i}  maxY:{maxY}')
    shape = getShape(n%5,maxY)
    desending = True
    while desending:
        if pattern[i%len(pattern)] == '<':  # left
            canMove = True
            for coord in shape:
                if coord[0] == 0:
                    canMove = False
            if canMove:
                for coord in shape:
                    if (coord[0]-1,coord[1]) in grid:
                        canMove = False
            if canMove:
                for coord in shape:
                    coord[0] -= 1
        else:
            canMove = True
            for coord in shape:
                if coord[0] == 6:
                    canMove = False
            if canMove:
                for coord in shape:
                    if (coord[0]+1,coord[1]) in grid:
                        canMove = False
            if canMove:
                for coord in shape:
                    coord[0] += 1
        i += 1

        canMove = True
        for coord in shape:
            if coord[1] == 0:
                canMove = False
        if canMove:
            for coord in shape:
                if (coord[0],coord[1]-1) in grid:
                    canMove = False

        if canMove:
            for coord in shape:
                coord[1] -= 1
            continue
        else:
            for coord in shape:
                grid.add((coord[0],coord[1]))
                if coord[1]+1 > maxY:
                    maxY = coord[1]+1
            desending = False
            n += 1

maxY += loopingTimes * 2616
print(maxY)

exit()
#Code used to find the diff values, printing in case it needs to cycle before repeating

numPrints = 0

#run until we find evidence of repeating
while numPrints < 100:
    shape = getShape(n%5,maxY)
    desending = True
    while desending:
        if pattern[i%len(pattern)] == '<':  # left
            canMove = True
            for coord in shape:
                if coord[0] == 0:
                    canMove = False
            if canMove:
                for coord in shape:
                    if (coord[0]-1,coord[1]) in grid:
                        canMove = False
            if canMove:
                for coord in shape:
                    coord[0] -= 1
        else:
            canMove = True
            for coord in shape:
                if coord[0] == 6:
                    canMove = False
            if canMove:
                for coord in shape:
                    if (coord[0]+1,coord[1]) in grid:
                        canMove = False
            if canMove:
                for coord in shape:
                    coord[0] += 1
        i += 1

        canMove = True
        for coord in shape:
            if coord[1] == 0:
                canMove = False
        if canMove:
            for coord in shape:
                if (coord[0],coord[1]-1) in grid:
                    canMove = False

        if canMove:
            for coord in shape:
                coord[1] -= 1
            continue
        else:
            for coord in shape:
                grid.add((coord[0],coord[1]))
                if coord[1] + 1 > maxY:
                    maxY = coord[1]+1
            desending = False
            n += 1

            if i % len(pattern) == iSnapshot and n % 5 == nSnapshot:
                print(f'n: {n}   maxY: {maxY}')
                print(f'diffs: n: {n-nSnapshop}')
                numPrints += 1
