file, boundNum= 'test.txt',20
file, boundNum= 'input.txt',4000000
#file, boundNum= 'JustinInput.txt',4000000
#file, boundNum= 'input',4000000
#boundNum += 1 #count the final row/column

with open(file) as inp:
    z = inp.read()
    z = z.strip()


numbers = []

def check(x,y,boundNum,x1,y1,dist):
    if x < 0 or y < 0 or x > boundNum or y > boundNum:
        return False
    answer = True
    for x1,x2,y1,y2,dist in numbers:
        if abs(x1-x) + abs(y1-y) <= dist:
            answer = False
            break
    return answer


for line in z.split('\n'):
    _,_,x1,y1,_,_,_,_,x2,y2 = line.split(' ')
    x1 = int(x1[2:-1])
    x2 = int(x2[2:-1])
    y1 = int(y1[2:-1])
    y2 = int(y2[2:])

    dist = abs(x2-x1) + abs(y2-y1)

    numbers.append((x1,x2,y1,y2,dist))


#I got this as a hint from the subreddit to look at a ring around each search space
possible = set()
for x1,x2,y1,y2,dist in numbers:
    dist += 1
    print(dist)
    for i in range(0,dist+1):
        if check(x1+dist-i,y1+i,boundNum,x1,y1,dist):
            print(x1+dist-i,y1+i)
            exit()
        if check(x1+dist-i,y1-i,boundNum,x1,y1,dist):
            print(x1+dist-i,y1-i)
            exit()
        if check(x1-dist+i,y1+i,boundNum,x1,y1,dist):
            print(x1-dist+i,y1+i)
            exit()
        if check(x1-dist+i,y1-i,boundNum,x1,y1,dist):
            print(x1-dist+i,y1-i)
            exit()

print((14,11) in possible)
print(len(possible))

"""for x,y in possible:
    if x < 0 or y < 0 or x > boundNum or y > boundNum:
        continue
    answer = True
    for x1,x2,y1,y2,dist in numbers:
        if abs(x1-x) + abs(y1-y) <= dist:
            answer = False
            break
    if answer:
        print(x,y)
        print(4000000*x + y)
        exit()
"""


#test code below
"""
grid = []
for i in range(0,21):
    grid.append([])
    for j in range(0,21):
        grid[-1].append(' ')

for x,y in possible:
    if x>= 0 and x <= 20 and y >= 0 and y <= 20:
        grid[y][x] = '*'

for row in grid:
    for column in row:
        print(column,end='')
    print()
exit()
"""

#relics below

"""
for x in range(0,boundNum):
    if x % 10 == 0:
        print(x)
    for y in range(0,boundNum):
        canBeBeacon = True
        for x1,x2,y1,y2,dist in numbers:
            if abs(x1-x) + abs(y1-y) <= dist:
                canBeBeacon = False
                break
        if canBeBeacon:
            print(4000000*x + y)
            exit()





#failed attempt below this, trying dumb option above
#find answer
for row in range(0,boundNum):
    if row % 10 == 0:
        print(row)
    rowList = []
    for i in range(0,boundNum):
        rowList.append(1)

    for x1,x2,y1,y2,dist in numbers:

        for i in range(0,dist+1-(abs(row-y1))):  # This was shotgun debugging to find this expression
            #print(f'i: {i}')
            if x1+i < boundNum:
                rowList[x1+i] = 0
            if x1-i >= 0:
                rowList[x1-i] = 0
    if sum(rowList) > 1:
        y = row
        x = rowList.index(1)
        print('WE ARE DONE')
        print(4000000*x+y)
        exit()
"""