file = 'test.txt'
#file = 'input.txt'

with open(file) as inp:
    x = inp.read()
    x = x.strip()

ans = 0

lines = x.split("\n")
for i in range(0,len(lines)//3):
    aset = set()
    bset = set()
    cset = set()
    for c in lines[3*i]:
        aset.add(c)
    for c in lines[3*i+1]:
        bset.add(c)
    for c in lines[3*i+2]:
        cset.add(c)
    shared = (aset&bset&cset).pop()

    if shared >= 'A' and shared <= 'Z':
        ans += 26 + ord(shared) - ord('A') + 1
    if shared >= 'a' and shared <= 'z':
        ans += ord(shared) - ord('a') + 1

    ans += 'abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ'.index(shared) + 1

print(ans)