f = open("input.txt", "r")

rules = []
curLine = f.readline()
while curLine != "\n":
    rules.append(curLine.strip().split("|"))
    curLine = f.readline()

updates = []

for line in f.readlines():
    updates.append(line.strip().split(","))

sum = 0
for update in updates:
    passing = True
    #check if each rule is passing
    for rule in rules:
        if not (rule[0] in update and rule[1] in update): 
            continue
        firstIndex = update.index(rule[0])
        secondIndex = update.index(rule[1])

        if firstIndex > secondIndex: 
            passing = False
            break
        
    if passing: 
        sum += int(update[int(len(update)/2)])

print(sum)