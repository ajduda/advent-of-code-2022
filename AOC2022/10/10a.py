with open("input.txt") as inp:
    z = inp.read()
    z = z.strip()

special = [20,60,100,140,180,220]

i = 0  # Cycles
x = 1  # Register
ans = 0

for lines in z.split('\n'):
    words = lines.split(' ')
    if words[0] == 'noop':
        i += 1
        if i in special:
            ans += x * i
            print(lines)
            print(x)
            print(ans)
    else:
        i += 1
        if i in special:
            ans += x * i
            print(lines)
            print(x)
            print(ans)
        i += 1
        if i in special:
            ans += x * i
            print(lines)
            print(x)
            print(ans)
        x += int(words[1])

print(ans)