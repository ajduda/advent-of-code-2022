with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

ans = 0

trees = []
scores = []
for line in x.split('\n'):
    trees.append([])
    scores.append([])
    for c in line:
        trees[-1].append(int(c))
        scores[-1].append(1)

maximumScore = 0

for y in range(1,len(trees)-1):
    for x in range(1,len(trees[0])-1):
        print(f'TESTING [{y}][{x}]')
        #up
        seen = 0
        h = -1
        maxH = trees[y][x]
        for i in range(1,y+1):
            if trees[y-i][x] >= -1:
                h = trees[y-i][x]
                seen += 1
                if h >= maxH:
                    break
                print(f"A:([{y-i},{x}]: {h} is seen)")
        scores[y][x] *= seen
        #down
        seen = 0
        h = 0
        for i in range(y+1,len(trees)):
            if trees[i][x] >= -1:
                h = trees[i][x]
                seen += 1
                if h >= maxH:
                    break
                print(f"B:([{i},{x}]: {h} is seen)")
        scores[y][x] *= seen
        #left
        seen = 0
        h = 0
        for i in range(1,x+1):
            if trees[y][x-i] >= -1:
                h = trees[y][x-i]
                seen += 1
                if h >= maxH:
                    break
                print(f"C:([{y},{x-i}]: {h} is seen)")
        scores[y][x] *= seen
        #right
        seen = 0
        h = 0
        for i in range(x+1,len(trees[0])):
            if trees[y][i] >= -1:
                h = trees[y][i]
                seen += 1
                if h >= maxH:
                    break
                print(f"D:([{y},{i}]: {h} is seen)")
        scores[y][x] *= seen
        if scores[y][x] > maximumScore:
            maximumScore = scores[y][x]
            print(f'({x},{y}) IS THE NEW BEST')


for row in scores:
    print(row)

print(maximumScore)