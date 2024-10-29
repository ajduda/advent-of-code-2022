file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

monkeys = {}
solvedMonkeys = {}

for line in z.split('\n'):
    left,right = line.split(': ')
    if right[0].isdigit():
        solvedMonkeys[left] = int(right)
    else:
        monkeys[left] = right

while len(monkeys) > 0:
    keysToRemove = []
    for key in monkeys:
        l,op,r = monkeys[key].split(' ')
        if l in solvedMonkeys and r in solvedMonkeys:
            l = solvedMonkeys[l]
            r = solvedMonkeys[r]
            if op == '+':
                solvedMonkeys[key] = l + r
            elif op == '-':
                solvedMonkeys[key] = l - r
            elif op == '*':
                solvedMonkeys[key] = l * r
            elif op == '/':
                solvedMonkeys[key] = l // r
            else:
                print('error')
                exit()
            keysToRemove.append(key)

    for key in keysToRemove:
        monkeys.pop(key)

print(solvedMonkeys['root'])