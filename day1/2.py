f = open("input.txt", "r")
lines = f.readlines()

leftList = []
rightList = []

for line in lines: 
    a, b = line.split()
    leftList.append(int(a))
    rightList.append(int(b))

total = 0

for num in leftList: 
    total += num * rightList.count(num)

print(total)
