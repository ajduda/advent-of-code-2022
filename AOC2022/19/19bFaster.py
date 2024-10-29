file = 'test.txt'
#file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

sections = z.split(':')
sections = sections[1:]

robots = []

for section in sections:
    robot = []
    for word in section.split(' '):
        if word.isdigit():
            robot.append(int(word))
    robots.append(robot[:6])

if len(robots) < 3:
    robots = robots[:2]
print(robots)

def findBest(time,ore,clay,obsidian,geode,blueprint,oreBots=1,clayBots=0,obsidianBots=0,geodeBots=0):
    global memoize
    if (time,ore,clay,obsidian,geode,oreBots,clayBots,obsidianBots,geodeBots) in memoize:
        return memoize[(time,ore,clay,obsidian,geode,oreBots,clayBots,obsidianBots,geodeBots)]
    if time == 0:
        return geode
    maxOre = max(blueprint[0],blueprint[1],blueprint[2],blueprint[4])
    maxClay = blueprint[3]
    maxObsidian = blueprint[5]
    best = 0
    constructedBestBot = False
    if ore >= blueprint[4] and obsidian >= blueprint[5]:
        temp = findBest(time-1,ore-blueprint[4]+oreBots,clay+clayBots,obsidian+obsidianBots-blueprint[5],geode+geodeBots,blueprint,oreBots,clayBots,obsidianBots,geodeBots+1)
        if temp > best:
            best = temp
        constructedBestBot = True
    else:
        if ore >= blueprint[2] and clay >= blueprint[3] and obsidianBots < maxObsidian:
            temp = findBest(time-1,ore-blueprint[2]+oreBots,clay+clayBots-blueprint[3],obsidian+obsidianBots,geode+geodeBots,blueprint,oreBots,clayBots,obsidianBots+1,geodeBots)
            if temp > best:
                best = temp
            constructedBestBot = True

        if not constructedBestBot:
            if ore >= blueprint[0] and oreBots < maxOre:
                temp = findBest(time-1,ore-blueprint[0]+oreBots,clay+clayBots,obsidian+obsidianBots,geode+geodeBots,blueprint,oreBots+1,clayBots,obsidianBots,geodeBots)
                if temp > best:
                    best = temp
            if ore >= blueprint[1] and clayBots < maxClay:
                temp = findBest(time-1,ore-blueprint[1]+oreBots,clay+clayBots,obsidian+obsidianBots,geode+geodeBots,blueprint,oreBots,clayBots+1,obsidianBots,geodeBots)
                if temp > best:
                    best = temp
            temp = findBest(time-1,ore+oreBots,clay+clayBots,obsidian+obsidianBots,geode+geodeBots,blueprint,oreBots,clayBots,obsidianBots,geodeBots)
            if temp > best:
                best = temp

    memoize[(time,ore,clay,obsidian,geode,oreBots,clayBots,obsidianBots,geodeBots)] = best
    return best

ans = 1


for robot in robots:
    memoize = {}
    best = findBest(32,0,0,0,0,robot)
    print(best)
    ans *= best

print(f'ANSWER: {ans}')