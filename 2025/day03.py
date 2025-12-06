
def part1():
    with open("input3.txt", "r") as f:
        lines = f.readlines()
    pairv =""
    result = 0
    for line in lines:
        largestvolt = 0
        strl = line.strip()
        for pos in range(len(strl)):
            dig = strl[pos]
            for dig2 in strl[pos+1:]:
                pairv = dig + dig2
                largestvolt = max(largestvolt,int(pairv))
                # print(largestvolt, int(pairv))

        result += int(largestvolt)
        # print(largestvolt , line, result)
    print(result)

def part2():
    # greedy algo
    with open("input3.txt", "r") as f:
        lines = f.readlines()
    total_joltage = 0
    for line in lines:
        line = line.strip()
        lenl = len(line)

        removabledig = lenl- 12
        highvolt = []
        for digit in line:
            if len(highvolt)> 0:
                while highvolt and removabledig > 0 and highvolt[len(highvolt)-1] < digit:
                    highvolt.pop()
                    removabledig -= 1
            highvolt.append(digit)

        while removabledig > 0:
            highvolt.pop()
            removabledig -= 1

        finhighvolt =""
        for i in range(12):
            finhighvolt += highvolt[i]
        total_joltage += int(finhighvolt)

    print(total_joltage)

def part21():
    with open("input3.txt", "r") as f:
        lines = f.readlines()
    total_joltage = 0
    for line in lines:
        line = line.strip()
        if len(line) < 12:
            print(line , "sdfs")
            continue

        finhighvolt = ""
        start = 0
        # print (line)
        for i in reversed(range(12)):
            # print(line)
            # print(line[start:-i])
            checkstr = line[start:-i]
            if i == 0:
                checkstr = line[start:]
            value = max(checkstr)
            start = line.find(value, start) + 1
            finhighvolt += value

        total_joltage += int(finhighvolt)
        # print( line)
        # print(finhighvolt)

    print( total_joltage)
part1()
part2()
part21()

