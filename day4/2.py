lines = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        lines.append(line.strip())

total = 0 
for x in range(1, len(lines) - 1):
    for y in range(1, len(lines[0]) - 1):
        if lines[x][y] != "A": continue

        upLeft = lines[x-1][y-1]
        upRight = lines[x-1][y + 1]
        
        downLeft = lines[x+1][y-1]
        downRight= lines[x+1][y+1]

        firstWord = upLeft + 'A' + downRight
        secondWord = upRight + 'A' + downLeft

        if (firstWord == 'MAS' or firstWord == 'SAM' or firstWord[::-1] == 'MAS' or firstWord[::-1] == 'SAM') and ((secondWord == 'MAS' or secondWord == 'SAM' or secondWord[::-1] == 'MAS' or secondWord[::-1] == 'SAM')):
            total += 1

print(total)    


