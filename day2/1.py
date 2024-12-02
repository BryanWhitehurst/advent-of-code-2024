def reportIsSafe(numList): 
    firstNum = numList[0]
    secondNum = numList[1]
    increasing = True

    if secondNum == firstNum: return False
    if abs(secondNum - firstNum) >= 4: return False
    if secondNum < firstNum: increasing = False
    for i in range(2, len(numList)):
        if increasing and numList[i] <= numList[i - 1]: 
            return False
        elif (not increasing) and numList[i] >= numList[i - 1]: 
            return False
        elif abs(numList[i] - numList[i - 1]) > 3  or abs(numList[i] - numList[i - 1]) == 0:
            return False
    
    return True
    
f = open("input.txt", "r")
lines = f.readlines()
reports = []
for line in lines: 
    report = []
    temp = line.split()
    for num in temp: 
        report.append(int(num))

    reports.append(report)

total = 0
for report in reports: 
    if reportIsSafe(report) == True:
        total += 1
        
print(total)