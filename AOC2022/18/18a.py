file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

coords = set()

for line in z.split('\n'):
    a,b,c = line.split(',')
    a = int(a)
    b = int(b)
    c = int(c)
    coords.add((a,b,c))

ans = 0

for coord in coords:
    x,y,z = coord
    if (x+1,y,z) not in coords:
        ans += 1
    if (x-1,y,z) not in coords:
        ans += 1
    if (x,y+1,z) not in coords:
        ans += 1
    if (x,y-1,z) not in coords:
        ans += 1
    if (x,y,z+1) not in coords:
        ans += 1
    if (x,y,z-1) not in coords:
        ans += 1

print(ans)