file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

pattern = z

#
#
#
#

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

for n in range(0,2022):
    #print(f'{n}:{maxY}')
    shape = getShape(n%5,maxY)
    desending = True
    while desending:
        if pattern[i] == '<':  # left
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
        elif pattern[i] == '>':  # RIGHT
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
        else:
            print('pattern error')
            exit()
        i += 1
        if i == len(pattern):
            i = 0

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

print(maxY)

#attempting to print grid
"""for y in range(maxY-1,-1,-1):
    s = ''
    for x in range(0,7):
        if (x,y) in grid:
            s += '#'
        else:
            s += ' '
    print(s)"""