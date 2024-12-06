import copy

lines = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        lines.append(list(line.strip()))

global startingX
global startingY
global directionMap
directionMap = {"up": "right", "right": "down", "down": "left", "left": "up"}

previousPosition = []
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == '^':
            startingX = x
            startingY = y

def findLoop(matrix): 
    direction = "up"
    currentX = startingX
    currentY = startingY
    visitedSet = set()
    visitedSet.add((startingX, startingY, direction))

    while(True): 
        if currentX == -1 or currentX == len(matrix):
            #no loop found
            return False

        if currentY == -1 or currentY == len(matrix[0]):
            #no loop found
            return False

        #change direction
        if matrix[currentX][currentY] == '#':
            visitedSet.remove((currentX, currentY, direction))
            currentX = previousPosition[0]
            currentY = previousPosition[1]
            
            direction = directionMap[direction]


        previousPosition = (currentX, currentY)

        if direction == "up":
            currentX -= 1

        if direction == "down":
            currentX += 1

        if direction == "right":
            currentY += 1

        if direction == "left":
            currentY -= 1

        if(currentX, currentY, direction) in visitedSet:
            return True
        
        visitedSet.add((currentX, currentY, direction)) 

obstacleCount = 0 
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i == startingX and j == startingY:
            continue
        deepCopy = copy.deepcopy(lines)
        deepCopy[i][j] = '#'

        if findLoop(deepCopy):
            obstacleCount += 1

print(obstacleCount)