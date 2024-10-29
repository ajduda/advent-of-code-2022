with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

ans = 0

trees = []
visible = []
for line in x.split('\n'):
    trees.append([])
    visible.append([])
    for c in line:
        trees[-1].append(int(c))
        visible[-1].append(0)

#  L -> R
for y in range(0,len(trees)):
    visible[y][0] = 1
    h = trees[y][0]
    for x in range(0,len(trees[0])):
        if trees[y][x] > h:
            h = trees[y][x]
            visible[y][x] = 1

#  R -> L
for y in range(0,len(trees)):
    visible[y][-1] = 1
    h = trees[y][-1]
    for x in range(len(trees[0])-1,-1,-1):
        if trees[y][x] > h:
            h = trees[y][x]
            visible[y][x] = 1


# Top -> Bottom
for x in range(0,len(trees[0])):
    visible[0][x] = 1
    h = trees[0][x]
    for y in range(0,len(trees)):
        if trees[y][x] > h:
            h = trees[y][x]
            visible[y][x] = 1

# Bottom -> Top
for x in range(0,len(trees[0])):
    visible[-1][x] = 1
    h = trees[-1][x]
    for y in range(len(trees)-1,-1,-1):
        if trees[y][x] > h:
            h = trees[y][x]
            visible[y][x] = 1


ans = 0
for row in visible:
    for val in row:
        ans += val

print(ans)