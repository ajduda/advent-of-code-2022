file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()


rates = {}       # the flow rate of the valve in the room
tunnels = {}     # the connectivity to other locations
distances = {}   # distance to go from one room to another, and then turn on the valve
scorers = set()  # We only care about valves that have flow rate > 0

numPlaces = 0

valvescore = 1        # Used to encode the valves into a binary number
valveEncoding = {}      # a lookup to get the int encoding from a valve
valveDecoding = {}  # a lookup to get the vavles from an int encoding

for line in z.split('\n'):
    words = line.split(' ')
    src = words[1]
    rate = int(words[4][5:-1])
    dest = []
    for i in range(9,len(words)):
        if words[i][-1] == ',':
            dest.append(words[i][:-1])
        else:
            dest.append(words[i])

    rates[src] = rate
    if rate > 0:
        scorers.add(src)
        valveEncoding[src] = valvescore  # Only encode valves that can score
        valveDecoding[valvescore] = src
        valvescore *= 2
    tunnels[src] = dest
    distances[src] = {}
    numPlaces += 1

#build distances

# All distances are offset by 1 to compensate going there, AND turning on the valve
for src in distances.keys():
    distances[src][src] = 1
    rooms = {src}
    depth = 2
    while len(distances[src]) < numPlaces:
        newRooms = set()
        for room in rooms:
            for tunnel in tunnels[room]:
                if tunnel in distances[src]:
                    continue
                newRooms.add(tunnel)
        for room in newRooms:
            distances[src][room] = depth

        rooms = newRooms
        depth += 1

#print(distances['AA'])

def encodeValves(valveSet):
    valveCode = 0
    for valve in valveSet:
        valveCode += valveEncoding[valve]
    return valveCode

def decodeValves(valveCode):
    valveSet = set()
    for i in range(0,len(scorers)):
        if valveCode & (1 << i) > 0:
            valveSet.add(valveDecoding[1 << i])
    return valveSet

def valvePressure(valveSet):
    ret = 0
    for valve in valveSet:
        ret += rates[valve]
    return ret

memoize = {}

def bestPossible(time,room,valveEncoding):
    if time < 0:
        print('ERROR: We hit the failsafe')
        exit()


    if (time,room,valveEncoding) in memoize:
        return memoize[(time,room,valveEncoding)]

    #print(f'calling with params ({time},{room},{valveEncoding})')

    valveSet = decodeValves(valveEncoding)
    myPressure = valvePressure(valveSet)
    closedValves = scorers - valveSet

    # below block is now redundant
    # Test case edge case, where we end with all openable valves open and waiting

    bestOption = 0
    for valve in closedValves:
        timeDiff = distances[room][valve]
        if timeDiff > time:
            continue
        tempSet = valveSet.copy()
        tempSet.add(valve)
        tempEncoding = encodeValves(tempSet)
        tempValue = bestPossible(time-timeDiff,valve,tempEncoding) + (timeDiff * myPressure)
        if tempValue > bestOption:
            bestOption = tempValue
 
    if bestOption == 0:  # everything is too far to help us, just wait out the clock for points
        memoize[(time,room,valveEncoding)] = time*myPressure
        return time*myPressure
    else:
        memoize[(time,room,valveEncoding)] = bestOption
        return bestOption

print(bestPossible(30,'AA',0))