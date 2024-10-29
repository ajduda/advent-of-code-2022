def move(headPos,myPos):
    
    if abs(headPos[0]-myPos[0]) < 2 and abs(headPos[1]-myPos[1]) < 2:
        return myPos
    
    if abs(headPos[0]-myPos[0]) == 2 and abs(headPos[1]-myPos[1]) < 2:
        if headPos[0] > myPos[0]:
            return [headPos[0]-1,headPos[1]]
        else:
            return [headPos[0]+1,headPos[1]]

    if abs(headPos[0]-myPos[0]) < 2 and abs(headPos[1]-myPos[1]) == 2:
        if headPos[1] > myPos[1]:
            return [headPos[0],headPos[1]-1]
        else:
            return [headPos[0],headPos[1]+1]

    if headPos[0] > myPos[0]:
        x = 1
    else:
        x = -1
    if headPos[1] > myPos[1]:
        y = 1
    else:
        y = -1
    return [myPos[0] + x, myPos[1] + y]



with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

rope = []
for i in range(0,10):
    rope.append([0,0])

tailVisited = {(0,0)}

for line in x.split('\n'):
    #print(rope)
    direction,length = line.split(' ')
    length = int(length)

    if direction == 'U':
        for i in range(0,length):
            rope[0][1] += 1
            for j in range(1, len(rope)):
                rope[j] = move(rope[j-1],rope[j])
                #print(rope)
            tailVisited.add((rope[-1][0],rope[-1][1]))

    if direction == 'D':
        for i in range(0,length):
            rope[0][1] -= 1
            for j in range(1, len(rope)):
                rope[j] = move(rope[j-1],rope[j])
                #print(rope)
            tailVisited.add((rope[-1][0],rope[-1][1]))

    if direction == 'L':
        for i in range(0,length):
            rope[0][0] -= 1
            for j in range(1, len(rope)):
                rope[j] = move(rope[j-1],rope[j])
                #print(rope)
            tailVisited.add((rope[-1][0],rope[-1][1]))

    if direction == 'R':
        for i in range(0,length):
            rope[0][0] += 1
            for j in range(1, len(rope)):
                rope[j] = move(rope[j-1],rope[j])
                #print(rope)
            tailVisited.add((rope[-1][0],rope[-1][1]))

#print(tailVisited)

print(len(tailVisited))
