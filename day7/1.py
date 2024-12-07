from itertools import product

lines = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        leftSide, rightSide = line.split(":")
        leftSide = [int(leftSide)]
        rightSide = rightSide.strip().split()
        rightSide  = [ int(x) for x in rightSide ]
        
        lines.append(leftSide + rightSide)

total = 0
for line in lines: 
    numOfOperators = len(line) - 2
    operatorCombos = [''.join(x) for x in product(['+', '*'], repeat = numOfOperators)]
    operatorCombos = [list(x) for x in operatorCombos]

    for combo in operatorCombos:
        result = line[0]
        curTotal = line[1]
        for i in range(2, len(line)):
            op = combo.pop(0)
            if op == '+':
                curTotal += line[i]
            elif op == '*': 
                curTotal *= line[i]
        if result == curTotal: 
            total += result
            break

print(total)
