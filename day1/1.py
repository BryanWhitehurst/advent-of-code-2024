f = open("input.txt", "r")
lines = f.readlines()

leftList = []
rightList = []

for line in lines: 
    a, b = line.split()
    leftList.append(int(a))
    rightList.append(int(b))

leftList.sort()
rightList.sort()

total = 0
for i in range(len(leftList)): 
    total += abs(leftList[i] - rightList[i])

print(total)
