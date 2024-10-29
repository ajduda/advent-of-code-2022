def offset(i):
    if i % 3 == 0:
        return -1
    if i % 3 == 1:
        return 0
    return 1

with open("input.txt") as inp:
    z = inp.read()
    z = z.strip()

i = -1  # Cycles
x = 1  # Register

for lines in z.split('\n'):

    words = lines.split(' ')
    
    if words[0] == 'noop':
        i += 1
        if i % 40 == 0:
            print()
        if abs(x - (i % 40)) > 1:
            print('.',end='')
        else:
            print('#',end='')
    else:
        i += 1
        if i % 40 == 0:
            print()
        if abs(x - (i % 40)) > 1:
            print('.',end='')
        else:
            print('#',end='')
        i += 1
        if i % 40 == 0:
            print()
        if abs(x - (i % 40)) > 1:
            print('.',end='')
        else:
            print('#',end='')
        x += int(words[1])