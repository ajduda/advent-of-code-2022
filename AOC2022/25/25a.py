file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

#convert SNAFU to base 10
for line in z.split('\n'):
    base = 1
    num = 0
    for i in range(len(line)-1,-1,-1):
        if line[i].isdigit():
            num += int(line[i]) * base
        elif line[i] == '-':
            num -= base
        elif line[i] == '=':
            num -= (base * 2)
        else:
            print(f'parsing error: {line[i]}')
        base *= 5
    ans += num

SNAFU = []

# convert to base 5
while ans > 0:
    SNAFU.insert(0,ans % 5)
    ans //= 5

for i in range(len(SNAFU)-1,-1,-1):
    if SNAFU[i] > 2:
        SNAFU[i] -= 5
        if i == 0:
            SNAFU.insert(0,1)
        else:
            SNAFU[i-1] += 1


for c in SNAFU:
    if c >= 0:
        print(c,end='')
    elif c == -1:
        print('-',end='')
    elif c == -2:
        print('=',end='')
    else:
        print('SNAFU error')
print()