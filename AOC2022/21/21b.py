file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

monkeysMaster = {}
solvedMonkeysMaster = {}

for line in z.split('\n'):
    left,right = line.split(': ')
    if left == 'humn':
        continue
    if left == 'root':
        rootCheck = right
        continue
    if right[:4] == 'humn':
        humnLine = line
        continue
    if right[0].isdigit():
        solvedMonkeysMaster[left] = int(right)
    else:
        monkeysMaster[left] = right


# derive all we can without us shouting anything
changed = True
while changed:
    changed = False
    keysToRemove = []
    for key in monkeysMaster:
        l,op,r = monkeysMaster[key].split(' ')
        if l in solvedMonkeysMaster and r in solvedMonkeysMaster:
            l = solvedMonkeysMaster[l]
            r = solvedMonkeysMaster[r]
            if op == '+':
                solvedMonkeysMaster[key] = l + r
            elif op == '-':
                solvedMonkeysMaster[key] = l - r
            elif op == '*':
                solvedMonkeysMaster[key] = l * r
            elif op == '/':
                solvedMonkeysMaster[key] = l // r
            else:
                print('error')
                exit()
            keysToRemove.append(key)

    for key in keysToRemove:
        monkeysMaster.pop(key)
        changed = True

#print(monkeysMaster)

lcheck,_,rcheck = rootCheck.split(' ')
# if lcheck in solvedMonkeysMaster:
#     print('lcheck')
# if rcheck in solvedMonkeysMaster:
#     print('rcheck')
# exit()

# In both the test and the input, rcheck is set, lcheck needs to be set to solve for humn

solvedMonkeysMaster[lcheck] = solvedMonkeysMaster[rcheck]
#print(solvedMonkeysMaster[rcheck])
#print(lcheck)
#in both test and input, it's something: humn - somethingElse

#print(humnLine)
l,_,op,r = humnLine.split(' ')
l = l[:-1]
monkeysMaster['humn'] = l + ' + ' + r

#print(monkeysMaster)

changed = True
while changed:
    changed = False
    keysToRemove = []
    keysToAdd = {}
    #print(monkeysMaster)
    for key in monkeysMaster:
        if key not in solvedMonkeysMaster:
            l,op,r = monkeysMaster[key].split(' ')
            if l in solvedMonkeysMaster and r in solvedMonkeysMaster:
                l = solvedMonkeysMaster[l]
                r = solvedMonkeysMaster[r]
                if op == '+':
                    solvedMonkeysMaster[key] = l + r
                elif op == '-':
                    solvedMonkeysMaster[key] = l - r
                elif op == '*':
                    solvedMonkeysMaster[key] = l * r
                elif op == '/':
                    solvedMonkeysMaster[key] = l // r
                else:
                    print('error 1')
                    exit()
                keysToRemove.append(key)
        else:
            #print(f'solving {key} = {monkeysMaster[key]}')
            keysToRemove.append(key)
            l,op,r = monkeysMaster[key].split(' ')
            #if l in solvedMonkeysMaster:
                #print(f'{l}: {solvedMonkeysMaster[l]}')
            #if r in solvedMonkeysMaster:
                #print(f'{r}: {solvedMonkeysMaster[r]}')
            #print(f'{key}: {solvedMonkeysMaster[key]}')
            if op == '+':
                newOp = '-'
            if op == '-':
                newOp = '+'
            if op == '*':
                newOp = '/'
            if op == '/':
                newOp = '*'
            if l not in solvedMonkeysMaster and r not in solvedMonkeysMaster:
                print('we got the case I thought I did not have to program')
                exit()
            elif l not in solvedMonkeysMaster:
                myVal = solvedMonkeysMaster[key]
                r = solvedMonkeysMaster[r]
                if newOp == '+':
                    solvedMonkeysMaster[l] = myVal + r
                elif newOp == '-':
                    solvedMonkeysMaster[l] = myVal - r
                elif newOp == '*':
                    solvedMonkeysMaster[l] = myVal * r
                elif newOp == '/':
                    solvedMonkeysMaster[l] = myVal // r
                else:
                    print('error 2')
                #print(f'solved {l} as {solvedMonkeysMaster[l]}')
            else:  # r not in solvedMonkeysMaster
                myVal = solvedMonkeysMaster[key]
                l = solvedMonkeysMaster[l]
                if newOp == '+':
                    solvedMonkeysMaster[r] = l - myVal
                elif newOp == '-':
                    solvedMonkeysMaster[r] = myVal - l
                elif newOp == '*':
                    solvedMonkeysMaster[r] = l // myVal
                elif newOp == '/':
                    solvedMonkeysMaster[r] = myVal // l
                else:
                    print('error 3')
                #print(f'solved {r} as {solvedMonkeysMaster[r]}')

    for key in keysToRemove:
        monkeysMaster.pop(key)
        changed = True
#print(solvedMonkeysMaster)
#print(monkeysMaster)
print(solvedMonkeysMaster['humn'])
