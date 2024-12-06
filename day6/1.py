lines = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        lines.append(line.strip())

currentX = 0
currentY = 0
direction = "up"
directionMap = {"up": "right", "right": "down", "down": "left", "left": "up"}
visitedSet = set()
previousPosition = []
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == '^':
            currentX = x
            currentY = y

visitedSet.add((currentX, currentY))

while(True): 
    if currentX == -1 or currentX == len(lines):
        visitedSet.remove((currentX, currentY)) 
        break

    if currentY == -1 or currentY == len(lines[0]):
        break

    #change direction
    if lines[currentX][currentY] == '#':
        visitedSet.remove((currentX, currentY))
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

    visitedSet.add((currentX, currentY)) 

print(len(visitedSet))