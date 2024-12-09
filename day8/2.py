import itertools

lines = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        lines.append(line.strip())

antenaTypes = set()
for line in lines:
    for char in line:
        if char == '.' or char == '\n':
            continue
        antenaTypes.add(char)
antenaDict = {}

for type in antenaTypes:
    antenaDict[type] = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if(lines[i][j] == '.'):
            continue

        antenaDict[lines[i][j]].append((i, j))

antinodeLocations = set()
for lst in antenaDict.values():
    allPairs = list(itertools.combinations(lst, 2))
    for pair in allPairs:
        leftNode = pair[0]
        rightNode = pair[1]

        antinodeLocations.add(leftNode)
        antinodeLocations.add(rightNode)

        antiNodeX1 = leftNode[0] + (leftNode[0] - rightNode[0])
        antiNodeY1 = leftNode[1] + (leftNode[1] - rightNode[1])
    
        while True: 
            if antiNodeX1 >= len(lines) or antiNodeX1 < 0 or antiNodeY1 >= len(lines[0]) or antiNodeY1 < 0:
                break
            
            antinodeLocations.add((antiNodeX1, antiNodeY1))

            antiNodeX1 += leftNode[0] - rightNode[0]
            antiNodeY1 += leftNode[1] - rightNode[1]
        
        antiNodeX2 = rightNode[0] + (rightNode[0] - leftNode[0])
        antiNodeY2 = rightNode[1] + (rightNode[1] - leftNode[1])

        while True:
            if antiNodeX2 >= len(lines) or antiNodeX2 < 0 or antiNodeY2 >= len(lines[0]) or antiNodeY2 < 0:
                break
            
            antinodeLocations.add((antiNodeX2, antiNodeY2))

            antiNodeX2 += rightNode[0] - leftNode[0]
            antiNodeY2 += rightNode[1] - leftNode[1]

print(len(antinodeLocations))