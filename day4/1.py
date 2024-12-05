def countDiags(matrix):
    total = 0

    x = 0
    while x < len(matrix):
        currentDiag = ""
        y = 0
        for i in range(x, -1, -1):
            if y == len(matrix[0]): break
            currentDiag += matrix[i][y]
            y += 1

        total += currentDiag.count("XMAS")
        total += currentDiag[::-1].count("XMAS")

        x += 1

    y = 1
    while y < len(matrix[0]):
        currentDiag = ""
        x = len(matrix) - 1
        for i in range(y, len(matrix[0])):
            if x == -1: break
            currentDiag += matrix[x][i]
            x -= 1

        total += currentDiag.count("XMAS")
        total += currentDiag[::-1].count("XMAS")
        y += 1 

    return total

def countRows(matrix):
    total = 0 
    for line in matrix:
        total += line.count("XMAS")
        total += line[::-1].count("XMAS")
    return total


lines = []
with open("input.txt", 'r') as current_file:
    for line in current_file.readlines():
        lines.append(line.strip())

rotated = [''.join(list(i)[::-1]) for i in zip(*lines)]
transposed = [''.join(s) for s in zip(*lines)]
total = 0
total += countRows(lines)
total += countRows(transposed)
total += countDiags(lines)
total += countDiags(rotated)

print(total)
