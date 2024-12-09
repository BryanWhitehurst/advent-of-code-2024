import numpy as np

def findMin(arr):
    min = arr[0][0]
    for subArray in arr:
       if subArray[0] < min:
          min = subArray[0]
    return min
f = open("input.txt", "r")
inp = f.readline()
inp = inp.strip()
memory = []

idNum = 0

fileLength = {}
freeSpaceLength = []
for i in range(len(inp)):
    #is even, represents file space
    if i % 2 == 0:
        if int(inp[i]) != 0: fileLength[idNum] = (len(memory), int(inp[i]))
        memory += [str(idNum) for x in range(int(inp[i]))]
        idNum += 1
    #represents free space
    else:
        if int(inp[i]) != 0: freeSpaceLength.append([len(memory), int(inp[i])])
        memory += ['.' for x in range(int(inp[i]))]

memory = np.array(memory)

#move file space over one block at a time
memoryKeys = list(fileLength.keys())
memoryKeys.reverse()

for key in memoryKeys: 
    #attempt to place in each available free space
    freeSpaceIndex = 0
    while True:
        if freeSpaceIndex == len(freeSpaceLength): break
        if fileLength[key][0] < freeSpaceLength[freeSpaceIndex][0]:
            break
        if fileLength[key][1] <= freeSpaceLength[freeSpaceIndex][1]:
            #replace the spot
            memory[freeSpaceLength[freeSpaceIndex][0]:freeSpaceLength[freeSpaceIndex][0]+fileLength[key][1]] = memory[fileLength[key][0]:fileLength[key][0] + fileLength[key][1]]
            memory[fileLength[key][0]:fileLength[key][0] + fileLength[key][1]] = ["." for _ in range(fileLength[key][1])]
            if fileLength[key][1] < freeSpaceLength[freeSpaceIndex][1]:
                freeSpaceLength[freeSpaceIndex][0] = freeSpaceLength[freeSpaceIndex][0] + fileLength[key][1]
                freeSpaceLength[freeSpaceIndex][1] -= fileLength[key][1]
            else: 
                freeSpaceLength.pop(freeSpaceIndex)
            
            break
        freeSpaceIndex += 1

total = 0
for i in range(len(memory)):
    if memory[i] == '.': continue

    total += i * int(memory[i])

print(total)