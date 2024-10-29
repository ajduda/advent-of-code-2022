file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

def printNice(numberList,numberOffsets):
    s = ''
    for i in range(0, len(numberList)):
        s += str(numberOffsets[numberList[i]])
        s += ' '
    print(s)


i = 0
numberOffsets = {}
numberList = []
for number in z.split('\n'):
    numberList.append(i)
    numberOffsets[i] = int(number) * 811589153
    if int(number) == 0:
        zeroKey = i
    i += 1

size = len(numberOffsets)
for _ in range(0,10):
    for i in range(0,size):
        #printNice(numberList, numberOffsets)
        number = numberOffsets[i]
        index = numberList.index(i)
        newIndex = (index + number)
        newIndex %= size - 1
        if newIndex == 0:
            newIndex = size-1
        numberList.pop(index)
        numberList.insert(newIndex,i)

#printNice(numberList, numberOffsets)
zeroIndex = numberList.index(zeroKey)
print(numberOffsets[numberList[(zeroIndex + 1000) % len(numberList)]])
print(numberOffsets[numberList[(zeroIndex + 2000) % len(numberList)]])
print(numberOffsets[numberList[(zeroIndex + 3000) % len(numberList)]])
print(numberOffsets[numberList[(zeroIndex + 1000) % len(numberList)]] +\
      numberOffsets[numberList[(zeroIndex + 2000) % len(numberList)]] +\
      numberOffsets[numberList[(zeroIndex + 3000) % len(numberList)]])