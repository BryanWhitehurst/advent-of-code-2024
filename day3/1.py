import re

f = open("input.txt", "r")
text = f.readline()
regex = "mul\(\d+,\d+\)"
output = re.findall(regex, text)
total = 0
for instruction in output:
    nums = re.findall("\d+", instruction)
    total += int(nums[0]) * int(nums[1])

print(total)