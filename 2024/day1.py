from collections import Counter

inputFile = open("input1.txt", "r")
lines = inputFile.read().strip().split("\n")
inputFile.close()

Left, Right = [], []
RC = Counter()

for line in lines:
    lefts,rights = line.split()
    left,right = int(lefts), int(rights)
    Left.append(left)
    Right.append(right)
    RC[right] += 1

sum = 0
Left.sort()
Right.sort()

locationList = zip(Left, Right)
for l,r in locationList:
    sum += abs(r-l)

print(sum)

similarityScpre = 0
for l in Left:
    similarityScpre += l*RC[l]
    print(l, RC[l], similarityScpre)
print(similarityScpre)