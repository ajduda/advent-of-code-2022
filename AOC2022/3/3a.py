with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

ans = 0

for line in x.split("\n"):
    length = len(line)//2
    l = line[0:length]
    r = line[length:]
    lset = set()
    rset = set()
    for i in l:
        lset.add(i)
    for i in r:
        rset.add(i)
    shared = (lset&rset).pop()

    if shared >= 'A' and shared <= 'Z':
        ans += 26 + ord(shared) - ord('A') + 1
    if shared >= 'a' and shared <= 'z':
        ans += ord(shared) - ord('a') + 1

    #ans += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(shared) + 1

print(ans)