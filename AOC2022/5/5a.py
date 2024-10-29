with open("input.txt") as inp:
    x = inp.read()
    #x = x.strip()

stacks = []
numStacks = len(x.split("\n")[0]) // 4
numStacks += 1
for i in range(0,numStacks):
    stacks.append([])

setup = True

for line in x.split("\n"):
    if len(line) == 0:
        continue
    if setup:
        if line[1] == '1':
            setup = False
            continue
        for i in range(0,numStacks):
            idx = 4*i + 1
            if line[idx] != ' ':
                stacks[i].insert(0,line[idx])
                
    else:  # moving things around
        words = line.split(" ") # moving x from y to z
        amt = int(words[1])
        src = int(words[3]) - 1
        dst = int(words[5]) - 1
        amt = (amt > len(src)) ? len(src) : amt
        for i in range(0,amt):
            x = stacks[src].pop()
            stacks[dst].append(x)

#print(stacks)
ans = ''
for stack in stacks:
    ans += stack.pop()

print(ans)