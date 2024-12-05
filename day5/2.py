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
notPassing = []
#find updates not passing
for update in updates:
    passing = True
    #check if each rule is passing
    for rule in rules:
        if not (rule[0] in update and rule[1] in update): 
            continue
        firstIndex = update.index(rule[0])
        secondIndex = update.index(rule[1])

        if firstIndex > secondIndex: 
            notPassing.append(update)
            break

for update in notPassing:
    i = 0
    while i < len(rules): 
        currentRule = rules[i]
        if (currentRule[0] in update and currentRule[1] in update): 
            firstIndex = update.index(currentRule[0])
            secondIndex = update.index(currentRule[1])

            #not passing, perform swap
            if firstIndex > secondIndex: 
                temp = update[firstIndex]
                update[firstIndex] = update[secondIndex]
                update[secondIndex] = temp

                #check all rules again
                i = 0
                continue
        
        i+= 1
    
    sum += int(update[int(len(update)/2)])

print(sum)
