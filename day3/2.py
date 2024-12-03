import re

f = open("input.txt", "r")
text = f.readline()
regex = "(don't\(\)|do\(\)|mul\(\d+,\d+\))"
output = re.findall(regex, text)
print(output)

total = 0
doMath = True
for str in output:
    if str == "do()":
        doMath = True

    if str == "don't()":
        doMath = False

    if not doMath: continue

    if str.startswith("mul"):
         nums = re.findall("\d+", str)
         total += int(nums[0]) * int(nums[1])

print(total)

