with open("input.txt") as inp:
    x = inp.read()
    x = x.strip()

score = 0

for line in x.split("\n"):
    l,r = line.split(" ")
    if r == 'X':
        score += 0
        if l == "A":
            score += 3
        if l == "B":
            score += 1
        if l == "C":
            score += 2
    elif r == "Y":
        score += 3
        if l == "A":
            score += 1
        if l == "B":
            score += 2
        if l == "C":
            score += 3
    elif r == "Z":
        score += 6
        if l == "A":
            score += 2
        if l == "B":
            score += 3
        if l == "C":
            score += 1
    #print(f'{line} : {score}')

print(score)
