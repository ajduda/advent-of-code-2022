file = 'test.txt'
file = 'input.txt'

extra = 10  # it needs to be 6 or greater to pass the input

with open(file) as inp:
    z = inp.read()
    z = z.strip()

coords = set()

#bounding box
x1 = 1000
x2 = -1000
y1 = 1000
y2 = -1000
z1 = 1000
z2 = -1000

for line in z.split('\n'):
    a,b,c = line.split(',')
    a = int(a)
    b = int(b)
    c = int(c)
    coords.add((a,b,c))
    x1 = min(x1,a)
    x2 = max(x2,a)
    y1 = min(y1,b)
    y2 = max(y2,b)
    z1 = min(z1,c)
    z2 = max(z1,c)

ans = 0

steam = {(x1-1,y1-1,z1-1)}

expanding = {(x1-1,y1-1,z1-1)}

while len(expanding) > 0:
    x,y,z = expanding.pop()
    if x > x1-extra:
        checking = (x-1,y,z)
        if checking not in steam and checking not in coords:
            steam.add(checking)
            expanding.add(checking)
    if x < x2+extra:
        checking = (x+1,y,z)
        if checking not in steam and checking not in coords:
            steam.add(checking)
            expanding.add(checking)
    if y > y1-extra:
        checking = (x,y-1,z)
        if checking not in steam and checking not in coords:
            steam.add(checking)
            expanding.add(checking)
    if y < y2+extra:
        checking = (x,y+1,z)
        if checking not in steam and checking not in coords:
            steam.add(checking)
            expanding.add(checking)
    if z > z1-extra:
        checking = (x,y,z-1)
        if checking not in steam and checking not in coords:
            steam.add(checking)
            expanding.add(checking)
    if z < z2+extra:
        checking = (x,y,z+1)
        if checking not in steam and checking not in coords:
            steam.add(checking)
            expanding.add(checking)



for coord in coords:
    x,y,z = coord
    if (x+1,y,z) in steam:
        ans += 1
    if (x-1,y,z) in steam:
        ans += 1
    if (x,y+1,z) in steam:
        ans += 1
    if (x,y-1,z) in steam:
        ans += 1
    if (x,y,z+1) in steam:
        ans += 1
    if (x,y,z-1) in steam:
        ans += 1

print(ans)