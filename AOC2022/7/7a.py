def mySize(myDir):
    ret = 0
    for fileSize in myDir[2].values():  # all the sizes only
        ret += fileSize
    for directory in myDir[1].values():
        ret += mySize(directory)
    return ret


with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

root = [False, {}, {}] #All directorys are stored like this: parent, children, files in directory
myDir = root

lines = x.split('\n')
i = 0
numLines = len(lines)
while i < numLines:
    words = lines[i].split(" ")
    if words[0] == '$':
        if words[1] == 'cd':
            dest = words[2]
            if dest == '/':
                myDir = root
            elif dest == '..':
                myDir = myDir[0]
            else:
                if dest not in myDir[1]: #create dir and move to it
                    newDir = [myDir, {}, {}]
                    myDir[1][dest] = newDir
                myDir = myDir[1][dest]  # This not in the if means we can move to existing dir.
            i += 1

        elif words[1] == 'ls':
            i += 1
            continue #handled in cd? if invalid commands come in I'm in trouble
        else:
            print("error 1")
            exit()

    else:
        if words[0] == 'dir':
            i += 1
            continue
        else:
            size = int(words[0])
            name = words[1]
            myDir[2][name] = size
            i += 1

ans = 0

directoriesToCheck = [root]
while len(directoriesToCheck) > 0:
    myDir = directoriesToCheck.pop()
    if mySize(myDir) < 100000:
        ans += mySize(myDir)
    for dirs in myDir[1].values():
        directoriesToCheck.append(dirs)

print(ans)
