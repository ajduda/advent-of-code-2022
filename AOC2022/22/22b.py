file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    #z = z.strip()

maze,commands = z.split('\n\n')

grid = [[]]
EMPTY = '.'
WALL = '#'
VOID = ' '


maxX = -1

for line in maze.split('\n'):
    grid.append([VOID])
    x = 1
    for c in line:
        grid[-1].append(c)
        x += 1
    grid[-1].append(VOID)
    x += 1
    if maxX < x:
        maxX = x
grid.append([])

for y in range(0,len(grid)):
    while len(grid[y]) < maxX:
        grid[y].append(VOID)


commandList = []
i = 0
while i < len(commands):
    if commands[i].isdigit():
        lbound = i
        i += 1
        while commands[i].isdigit():
            i += 1
        commandList.append(int(commands[lbound:i]))
    else:
        commandList.append(commands[i])
        i += 1

commandList.pop()  # Trailing newline, which also lets the last command be a number without a bounds check

#print(commandList)


y = 1
x = 0
while grid[y][x] != EMPTY:
    x += 1


"""print(y,x)
for y in range(0,len(grid)):
    for x in range(0,len(grid[y])):
        print(grid[y][x],end='')
    print()
"""

direction = 0  # unit circle directions, in units of PI/2: R = 0, U = 1, L = 2, D = 3
print(f'(x,y) = ({x},{y})')
for command in commandList:
    if type(command) == type(7):
        if direction == 0:
            dx = 1
            dy = 0
        elif direction == 1:
            dx = 0
            dy = -1
        elif direction == 2:
            dx = -1
            dy = 0
        elif direction == 3:
            dx = 0
            dy = 1
        else:
            print('direction error')
            exit()

        for i in range(0,command):
            if grid[y+dy][x+dx] == VOID:
                #warp case (unless there is a wall on the other side)
                #Warping along cube is weird. Cube is laid out like this (using white top green front rubic's cube notation):
                #  WR
                #  G
                # OY
                # B 

                # each is represented upright under these conditions:
                #   W is upright when B is above
                #   G is upright when W is above
                #   Y is upright when G is above
                #   R is upright when B is above
                #   O is upright when G is above
                #   B is upright when O is above
                # because of my padding, bounds will be from 1 to 50, 51 to 100, 101 to 150, 151 to 200
                # For when I set the coord specifically, I'll include the endpoints in a comment to justify that formula


                # We don't have to consider these as x + dx, y + dy because the direction check covers that, simplifying the code a little here

                if direction == 0 and 1 <= y and y <= 50:  # R -> Y
                    newDir = 2
                    newX = 100
                    newY = 151 - y  # 1 -> 150, 50 -> 101
                elif direction == 0 and 51 <= y and y <= 100:  # G -> R
                    newDir = 1
                    newX = y + 50  # 51 -> 101, 100 -> 150
                    newY = 50
                elif direction == 0 and 101 <= y and y <= 150:  # Y -> R
                    newDir = 2
                    newX = 150
                    newY = 151 - y  # 101 -> 50, 150 -> 1
                elif direction == 0 and 151 <= y and y <= 200:  # B -> Y
                    newDir = 1
                    newX = y - 100  # 151 -> 51, 200 -> 100
                    newY = 150
                elif direction == 1 and 1 <= x and x <= 50:  # O -> G
                    newDir = 0
                    newX = 51
                    newY = x + 50  # 1 -> 51, 50 -> 100
                elif direction == 1 and 51 <= x and x <= 100:  # W -> B
                    newDir = 0
                    newX = 1
                    newY = x + 100 # 51 -> 151, 100 -> 200
                elif direction == 1 and 101 <= x and x <= 150:  # R -> B
                    newDir = 1
                    newX = x - 100  # 101 -> 1, 150 -> 50
                    newY = 200
                elif direction == 2 and 1 <= y and y <= 50:  # W -> G
                    newDir = 0
                    newX = 1
                    newY = 151 - y  # 1 -> 150, 50 -> 101
                elif direction == 2 and 51 <= y and y <= 100:  # G -> O
                    newDir = 3
                    newX = y - 50  # 51 -> 1, 100 -> 50
                    newY = 101
                elif direction == 2 and 101 <= y and y <= 150:  # O -> W
                    newDir = 0
                    newX = 51
                    newY = 151 - y  # 101 -> 50, 150 -> 1
                elif direction == 2 and 151 <= y and y <= 200:  # B -> W
                    newDir = 3
                    newX = y - 100  # 151 -> 51, 200 -> 100
                    newY = 1
                elif direction == 3 and 1 <= x and x <= 50:  # B -> R
                    newDir = 3
                    newX = x + 100  # 1 ->101, 50 -> 150
                    newY = 1
                elif direction == 3 and 51 <= x and x <= 100:  # Y -> B 
                    newDir = 2
                    newX = 50
                    newY = x + 100  # 51 -> 151, 100 -> 200
                elif direction == 3 and 101 <= x and x <= 150:  # R -> G
                    newDir = 2
                    newX = 100
                    newY = x - 50  # 101 -> 51, 150 -> 100
                else:
                    print(f'error, direction = {direction}, x = {x}, y = {y}, not doable')
                    exit()

                # begin sanity check section
                if newDir == 0:
                    tempDx = 1
                    tempDy = 0
                elif newDir == 1:
                    tempDx = 0
                    tempDy = -1
                elif newDir == 2:
                    tempDx = -1
                    tempDy = 0
                elif newDir == 3:
                    tempDx = 0
                    tempDy = 1
                else:
                    print('newDir value error')

                if grid[newY-tempDy][newX - tempDx] != VOID:
                    print('We are not at the bounds')
                    print(f'direction, x, y: {direction} ({x},{y}) -> {newDir} ({newX},{newY})')
                    exit()
                # end sanity check section

                if grid[newY][newX] == VOID:
                    print('you goofed, we are not on the cube')
                    print(f'direction, x, y: {direction} ({x},{y}) -> {newDir} ({newX},{newY})')
                    exit()
                if grid[newY][newX] == WALL:
                    break

                print(f'Went from ({x},{y}), dir = {direction} to ({newX},{newY}), dir = {newDir}')

                y = newY
                x = newX
                direction = newDir
                #new direction means we have to set dx,dy again
                if direction == 0:
                    dx = 1
                    dy = 0
                elif direction == 1:
                    dx = 0
                    dy = -1
                elif direction == 2:
                    dx = -1
                    dy = 0
                elif direction == 3:
                    dx = 0
                    dy = 1
                else:
                    print('direction error')
                    exit()

            else:
                if grid[y+dy][x+dx] == WALL:
                    break
                elif grid[y+dy][x+dx] == EMPTY:
                    y += dy
                    x += dx
        print(f'(x,y) = ({x},{y})')


    else:
        if command == 'R':
            direction -= 1
        elif command == 'L':
            direction += 1
        else:
            print('rotating command error')
            exit()
        direction %= 4


# I did the wrong values for the direction lol
if direction == 1:
    direction = 3
elif direction == 3:
    direction = 1

print(x,y,direction)
print(1000*y + 4*x + direction)