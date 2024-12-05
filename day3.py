import re

inputFile = open("input3.txt", "r")
lines2 = inputFile.read().split("\n")
sum1 = 0
pattern = re.compile(r'mul\((\d{1,4}),(\d{1,4})\)')
for line in lines2:
    matches = pattern.findall(line)
    # print (matches)
    for number in matches:
        # print (number)
        # print (int(number[0]) * int(number[1]))
        sum1 += int(number[0]) * int(number[1])
print (sum1)


sum2 = 0
sum3 = 0
enabled = True
for line in lines2:
    for i in range(len(line)):
        if line[i:].startswith('do()'):
            enabled = True
        if line[i:].startswith("don't()"):
            enabled = False
        matches = pattern.match(line[i:])
        if matches is not None:
            # print(matches.group(1), matches.group(2))
            sum3 += int(matches.group(1)) * int(matches.group(2))
            if enabled:
                sum2 += int(matches.group(1)) * int(matches.group(2))

print (sum2)


# 77055967
