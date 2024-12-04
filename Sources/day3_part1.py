import re
regex = r"(?<=mul\()\d+(?:,)\d+(?=\))"

data = open('Inputs\day3.txt', 'r').read()
matches_regex = re.finditer(regex, data, re.MULTILINE)
result = 0
for number, match in enumerate(matches_regex, start=1):
    values = str(match.group()).split(',')
    mul = int(values[0]) * int(values[1])
    result += mul
print("The results of the enabled multiplications is:", result) #187194524