f = open("input.txt", "r")
inp = f.readline()
inp = inp.strip()
memory = []

idNum = 0

for i in range(len(inp)):
    #is even, represents file space
    if i % 2 == 0:
        memory += [str(idNum) for x in range(int(inp[i]))]
        idNum += 1
    #represents free space
    else:
        memory += ['.' for x in range(int(inp[i]))]

#move file space over one at a time
leftPointer = memory.index('.')
rightPointer = len(memory) - 1

while leftPointer < rightPointer:
    if memory[leftPointer] != '.':
        leftPointer += 1
        continue

    if memory[rightPointer] == '.':
        rightPointer -= 1
        continue

    temp = memory[leftPointer]
    memory[leftPointer] = memory[rightPointer]
    memory[rightPointer] = temp

    leftPointer += 1
    rightPointer -= 1

total = 0
for i in range(len(memory)):
    if memory[i] == '.': break

    total += i * int(memory[i])

print(total)