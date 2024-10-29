file = 'test.txt'
#file = 'input.txt'

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

#memoize = {}

def bestPossible(time,room1,room2,valveEncoding,travel1,travel2):
    if time < 0:
        print('ERROR: We hit the failsafe')
        exit()

    if time == 0:
        return 0

    #if (time,room1,room2,valveEncoding,travel1,travel2) in memoize:
        #return memoize[(time,room1,room2,valveEncoding,travel1,travel2)]

    valveSet = decodeValves(valveEncoding)

    if travel1 == 0:
        if room1 in scorers:  # fix 'AA' poluting the valves
            valveSet.add(room1)
    if travel2 == 0:
        if room2 in scorers:
            valveSet.add(room2)
    myPressure = valvePressure(valveSet)
    closedValves = scorers - valveSet

    bestOption = 0

    if travel1 == 0 and travel2 == 0:
        for valve1 in closedValves:
            for valve2 in closedValves:
                tempTravel1 = distances[room1][valve1]
                tempTravel2 = distances[room2][valve2]
                dt = min(tempTravel1,tempTravel2)

                if dt > time:
                    continue

                tempEncoding = encodeValves(valveSet)
                tempValue = bestPossible(time-dt,valve1,valve2,tempEncoding,tempTravel1-dt,tempTravel2-dt)+(dt*myPressure)
                if tempValue > bestOption:
                    bestOption = tempValue

    elif travel1 == 0:
        for valve in closedValves:
            #if valve == room2:
                #continue  # elephant is heading there already
            tempTravel = distances[room1][valve]
            dt = min(tempTravel, travel2)

            if dt > time:
                continue

            tempEncoding = encodeValves(valveSet)
            tempValue = bestPossible(time-dt,valve,room2,tempEncoding,tempTravel-dt,travel2-dt)+(dt*myPressure)
            if tempValue > bestOption:
                bestOption = tempValue

    elif travel2 == 0:
        for valve in closedValves:
            #if valve == room1:
                #continue  # I am heading there already
            tempTravel = distances[room2][valve]
            dt = min(tempTravel,travel1)

            if dt > time:
                continue

            tempEncoding = encodeValves(valveSet)
            tempValue = bestPossible(time-dt,room1,valve,tempEncoding,travel1-dt,tempTravel-dt)+(dt*myPressure)
            if tempValue > bestOption:
                bestOption = tempValue

    else:  # travel1 OR travel2 should be 0, if neither are this should fail
        print('ERROR: travel misuse')
        exit()

    if bestOption == 0:
        return time * myPressure
    else:
        return bestOption

print(bestPossible(26,'AA','AA',0,0,0))