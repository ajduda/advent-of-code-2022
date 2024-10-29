with open("input.txt") as inp:
    z = inp.read()
    z = z.strip()

monkeys = []

for monkey in z.split('\n\n'):
    monkeys.append({})
    lines = monkey.split('\n')

    monkeys[-1]['items'] = []
    items = lines[1].split(': ')[1]
    for item in items.split(', '):
        monkeys[-1]['items'].append(int(item))
    
    monkeys[-1]['op'] = lines[2].split(' = ')[1]

    monkeys[-1]['test'] = int(lines[3].split(' ')[-1])

    monkeys[-1][True] = int(lines[4].split(' ')[-1])

    monkeys[-1][False] = int(lines[5].split(' ')[-1])

    monkeys[-1]['inspected'] = 0


primes = set()

for monkey in monkeys:
    primes.add(monkey['test'])

modulo = 1
for prime in primes:
    modulo *= prime

for i in range(0, 10000):
    if i % 10 == 0:
        print(i)
    for monkey in monkeys:
        #print(monkey)
        for item in monkey['items']:
            monkey['inspected'] += 1
            _,op,val = monkey['op'].split(' ')
            if val == 'old':
                val = item
            else:
                val = int(val)
            if op == '+':
                item += val
            elif op == '*':
                item *= val
            else:
                print('error, opval')
                exit
            item = item % modulo
            toMonkey = monkey[item%monkey['test']==0]
            monkeys[toMonkey]['items'].append(item)
        monkey['items'] = []

inspectedList = []
for monkey in monkeys:
    inspectedList.append(monkey['inspected'])

print(inspectedList)

inspectedList.sort()
print(inspectedList[-1]*inspectedList[-2])