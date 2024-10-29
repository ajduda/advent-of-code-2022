file = 'test.txt'
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
#start = [0,0]  # (y,x) to be consistant with how I store the grid
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
        #print(x,y)
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
                if direction == 0:
                    n = 0
                    while grid[y][n] == VOID:
                        n += 1
                    if grid[y][n] == WALL:
                        break
                    else:
                        x = n
                elif direction == 1:
                    n = len(grid)-1
                    while grid[n][x] == VOID:
                        n -= 1
                    if grid[n][x] == WALL:
                        break
                    else:
                        y = n
                elif direction == 2:
                    n = len(grid[y])-1
                    while grid[y][n] == VOID:
                        n -= 1
                    if grid[y][n] == WALL:
                        break
                    else:
                        x = n
                elif direction == 3:
                    n = 0
                    while grid[n][x] == VOID:
                        n += 1
                    if grid[n][x] == WALL:
                        break
                    else:
                        y = n
                else:
                    print('direction error two')
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