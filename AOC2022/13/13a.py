def parse(s):  # returns [index,list]
    ret = []
    i = 1

    while i < len(s):
        if s[i] == ']':
            return [i,ret]
        elif s[i].isdigit():
            lIndex = i
            while s[i].isdigit():
                i += 1
            ret.append(int(s[lIndex:i]))
        elif s[i] == ',':
            i += 1
        elif s[i] == '[':
            temp = parse(s[i:])
            ret.append(temp[1])
            i += temp[0] + 1

    print('how did we reach this?')
    exit()

def isCorrect(left,right):
    i = 0
    while True:
        if len(left) == i and len(right) == i:
            return None
        if len(left) == i:
            return True
        if len(right) == i:
            return False
        l = left[i]
        r = right[i]
        print(f'left: {left}')
        print(f'right: {right}')
        print(f'i: {i}')
        print(f'l: {l}')
        print(f'r: {r}')
        if type(l) is type(8):
            if type(r) is type(9):
                if l > r:
                    return False
                elif l == r:
                    i += 1
                elif l < r:
                    return True
            else:  # r is a list, listify l
                left[i] = [l]
        else:  # l is a list and thank you Nick
            if type(r) is type(13):
                right[i] = [r]
            else:  # l and r are lists!
                temp = isCorrect(l,r)
                if temp is not None:
                    return temp
                i += 1




with open("input.txt") as inp:
    z = inp.read()
    z = z.strip()

ans = 0
i = 1

for pair in z.split('\n\n'):
    left,right = pair.split('\n')
    left = parse(left)[1]
    right = parse(right)[1]
    #print(left)
    #print(right)

    if isCorrect(left,right):
        ans += i
        print(pair)
        print()

    i += 1

print(ans)