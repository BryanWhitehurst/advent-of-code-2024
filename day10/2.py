import copy
global matrix
matrix = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        arr = [int(x) for x in line.strip()]
        matrix.append(arr) 
        

#number of distinct trails vs number of nines reached
#we need to track each split off and then determine if that split off reaches a 9
#curPath is an array with the path
        
global totalPaths
def findNine(curNode, setOfNines, curPath):
    if matrix[curNode[0]][curNode[1]] == 9:
        totalPaths.append(curPath)
        return
    
    if (curNode[0] - 1 >= 0) and (curNode[0] - 1) < len(matrix) and matrix[curNode[0] - 1][curNode[1]] == 1 + matrix[curNode[0]][curNode[1]]:
        aCopy = copy.deepcopy(curPath)
        aCopy.append((curNode[0] - 1,curNode[1]))
        findNine((curNode[0] - 1,curNode[1]), setOfNines, aCopy)

    if (curNode[0] + 1) >= 0 and (curNode[0] + 1) < len(matrix) and matrix[curNode[0] + 1][curNode[1]] == 1 + matrix[curNode[0]][curNode[1]]:
        aCopy = copy.deepcopy(curPath)
        aCopy.append((curNode[0] + 1,curNode[1]))
        findNine((curNode[0] + 1,curNode[1]), setOfNines, aCopy)
    
    if (curNode[1] - 1) >= 0 and (curNode[1] - 1) < len(matrix[0]) and matrix[curNode[0]][curNode[1] - 1] == 1 + matrix[curNode[0]][curNode[1]]:
        aCopy = copy.deepcopy(curPath)
        aCopy.append((curNode[0],curNode[1] - 1))
        findNine((curNode[0],curNode[1] - 1), setOfNines, aCopy)

    if (curNode[1] + 1) >= 0 and (curNode[1] + 1) < len(matrix[0]) and matrix[curNode[0]][curNode[1] + 1] == 1 + matrix[curNode[0]][curNode[1]]:
        aCopy = copy.deepcopy(curPath)
        aCopy.append((curNode[0],curNode[1] + 1))
        findNine((curNode[0],curNode[1] + 1), setOfNines, aCopy)

zeroLocations = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            zeroLocations.append((i, j))

total = 0
for location in zeroLocations:
    nineSet = set()
    totalPaths = []
    findNine(location, nineSet, copy.deepcopy([location]))

    total += len(totalPaths)

print(total)