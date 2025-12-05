from collections import deque
import time

def load(file):
    filehandle = open(file)
    line = filehandle.read().strip().split()

    return line


# If you have an arrangement of five stones engraved with the numbers 0 1 10 99 999 and you blink once, the stones transform as follows:

# The first stone, 0, becomes a stone marked 1.
# The second stone, 1, is multiplied by 2024 to become 2024.
# The third stone, 10, is split into a stone marked 1 followed by a stone marked 0.
# The fourth stone, 99, is split into two stones marked 9.
# The fifth stone, 999, is replaced by a stone marked 2021976.

def part1():
    line = load('input11.txt')
    line = [int(x) for x in line]
    loop = 0
    newline = []
    timetaken =0
    while True:
        loop += 1
        if loop > 25:
            break

        starttime = time.time()
        print(f'\r loop {loop} and length {len(line)} taking time {timetaken}s', end="")

        for i, number in enumerate(line):

            strNumber = str(number)
            lenStr = len(strNumber)
            if number == 0:
                newline.append(1)
            elif lenStr % 2 == 0:
                first = int(strNumber[:lenStr // 2])
                second = int(strNumber[lenStr // 2:])
                newline.append(first)
                newline.append(second)
            else:
                numb = number * 2024
                newline.append(numb)
        line = newline
        newline = []
        timetaken = int(time.time() - starttime)
    print()
    print("All Stones count", len(line))

def getStones(numberin,loops,myStore):


    if loops == 0:
        return 1

    number = numberin
    print(f'\r processing {number}', end="")
    strNumber = str(number)
    lenStr = len(strNumber)
    if (numberin, loops) in myStore:
        lenNewline= myStore[(numberin, loops)]
    elif number == 0:
        lenNewline = getStones(1,loops-1,myStore)
    elif lenStr % 2 == 0:
        first = int(strNumber[:lenStr // 2])
        second = int(strNumber[lenStr // 2:])
        lenNewline=getStones(first,loops-1,myStore)
        lenNewline+= getStones(second,loops-1,myStore)
    else:
        numb = number * 2024
        lenNewline= getStones(numb,loops-1,myStore)

    print(f'\r loop {loops} and number {numberin} and length {lenNewline} ', end="")
    myStore[(numberin, loops)] = lenNewline

    return lenNewline

def part2():
    input = load('input11.txt')
    line = [int(x) for x in input]
    singlesNumber = 0
    mystore = {}
    for singleNumber in line:
        singlesNumber += getStones(singleNumber,75,mystore)
        print ( " and store count " ,mystore.__len__())
    print(f"\nAll stones count",singlesNumber)

startt = time.time()
part1()
part1time = time.time()-startt
print("time taken part1", part1time )
startt = time.time()
part2()
part2time = time.time()-startt
# print("time taken part2", part2time )
