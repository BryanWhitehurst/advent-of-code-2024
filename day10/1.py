global matrix
matrix = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        arr = [int(x) for x in line.strip()]
        matrix.append(arr) 
        

def findNine(curNode, setOfNines):
    if matrix[curNode[0]][curNode[1]] == 9:
        setOfNines.add(curNode)
        return
    
    if (curNode[0] - 1 >= 0) and (curNode[0] - 1) < len(matrix) and matrix[curNode[0] - 1][curNode[1]] == 1 + matrix[curNode[0]][curNode[1]]:
        findNine((curNode[0] - 1,curNode[1]), setOfNines)

    if (curNode[0] + 1) >= 0 and (curNode[0] + 1) < len(matrix) and matrix[curNode[0] + 1][curNode[1]] == 1 + matrix[curNode[0]][curNode[1]]:
        findNine((curNode[0] + 1,curNode[1]), setOfNines)
    
    if (curNode[1] - 1) >= 0 and (curNode[1] - 1) < len(matrix[0]) and matrix[curNode[0]][curNode[1] - 1] == 1 + matrix[curNode[0]][curNode[1]]:
        findNine((curNode[0],curNode[1] - 1), setOfNines)
    
    if (curNode[1] + 1) >= 0 and (curNode[1] + 1) < len(matrix[0]) and matrix[curNode[0]][curNode[1] + 1] == 1 + matrix[curNode[0]][curNode[1]]:
        findNine((curNode[0],curNode[1] + 1), setOfNines)


zeroLocations = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            zeroLocations.append((i, j))

total = 0
for location in zeroLocations:
    nineSet = set()
    findNine(location, nineSet)

    total += len(nineSet)

print(total)