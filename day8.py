import time
from http.cookiejar import offset_from_tz_string

def load():

    file = "input8.csv"
    # file = "test"
    inputfile = open(file, "r")
    lines = inputfile.read().strip().split("\n")
    linenumber = len(lines)
    print ("rows",linenumber, "cols", len(lines[0]))
    return lines,linenumber

def antennasLoad(lines):
    antennas = dict([])
    rownumber = 0
    for line in lines:
        colNumber = 0
        for data in line:
            if data != '.' :
                if data not in antennas:
                    antennas[data] = []
                antennas[data].append([rownumber, colNumber])
            colNumber += 1
        rownumber += 1
    # print(antennas)
    return antennas

def part1():
    lines,linenumber=load()
    antennas =antennasLoad(lines)
    antinodes = dict([])
    colNumber = len(lines[0])
    for value in antennas:
        for i in range(len(antennas[value])):
            for j in range(i,len(antennas[value])):
                if antennas[value][i] != antennas[value][j]:
                    # y2-y1/x2-x1
                    possiblepositions = []
                    if antennas[value][i][1] == antennas[value][j][1]:

                        for k in range(linenumber):  # y
                            for l in range(colNumber):  # x
                                if not(k == antennas[value][i][0] and l == antennas[value][i][1]) and not(k == antennas[value][j][0] and l == antennas[value][j][1]):
                                        possiblepositions.append([k, antennas[value][i][1]])
                    else:
                        slope1 = (antennas[value][i][0] - antennas[value][j][0]) / (antennas[value][i][1] - antennas[value][j][1])
                        offset = antennas[value][i][0] - slope1 * antennas[value][i][1]

                    for k in range(linenumber): #y
                        for l in range(colNumber):#x
                            if not(k == antennas[value][i][0] and l == antennas[value][i][1] ) and not( k == antennas[value][j][0] and l == antennas[value][j][1]):

                                if k == round(slope1 * l + offset,10):
                                    # print(k, l, slope1, offset, slope1 * l + offset)
                                    possiblepositions.append([k,l])

                    for position in possiblepositions:
                        if position in antennas[value]:
                            continue
                        row,col = position
                        if row >= 0 and row < linenumber and col >= 0 and col < colNumber:
                            if abs(row - antennas[value][i][0]) + abs(col - antennas[value][i][1]) == 2 * (abs(row - antennas[value][j][0]) + abs(col - antennas[value][j][1])):
                                if (row-antennas[value][i][0]) * (col-antennas[value][j][1]) == (row-antennas[value][j][0]) * (col-antennas[value][i][1]):
                                    if value not in antinodes:
                                        antinodes[value] = []
                                    antinodes[value].append(position)
                            if (abs(row - antennas[value][i][0]) + abs(col - antennas[value][i][1])) * 2  == (abs(row - antennas[value][j][0]) + abs(col - antennas[value][j][1])):
                                if (row - antennas[value][i][0]) * (col - antennas[value][j][1]) == (row - antennas[value][j][0]) * (col - antennas[value][i][1]):
                                    if value not in antinodes:
                                        antinodes[value] = []
                                    antinodes[value].append(position)

    uniquenodes = set()
    for value in antinodes:
        for position in antinodes[value]:
            uniquenodes.add(tuple(position))
    sumPart1 = len(uniquenodes)
    print_matrix(uniquenodes, lines)
    print_matrix(uniquenodes, lines)
    print(sumPart1)



def print_matrix(uniquenodes, lines):

    for v in uniquenodes:
        linelist=list(lines[v[0]])
        if linelist[v[1]] == '.':
            linelist[v[1]] = 'X'
        else:
            linelist[v[1]] = '#'
        lines[v[0]] = ''.join(linelist)
    for line in lines:
        print(line)






def part2():
    lines,linenumber=load()
    antennas =antennasLoad(lines)
    antinodes = dict([])
    colNumber = len(lines[0])
    for value in antennas:
        for i in range(len(antennas[value])):
            for j in range(i,len(antennas[value])):
                if antennas[value][i] != antennas[value][j]:
                    # y2-y1/x2-x1
                    possiblepositions = []
                    if antennas[value][i][1] == antennas[value][j][1]:

                        for k in range(linenumber):  # y
                                possiblepositions.append([k, antennas[value][i][1]])
                    else:
                        slope1 = (antennas[value][i][0] - antennas[value][j][0]) / (antennas[value][i][1] - antennas[value][j][1])
                        offset = antennas[value][i][0] - slope1 * antennas[value][i][1]

                        for k in range(linenumber): #y
                            for l in range(colNumber):#x
                                    if k == round(slope1 * l + offset,10):
                                        possiblepositions.append([k,l])

                    for position in possiblepositions:
                        row,col = position
                        if row >= 0 and row < linenumber and col >= 0 and col < colNumber:
                            if (row-antennas[value][i][0]) * (col-antennas[value][j][1]) == (row-antennas[value][j][0]) * (col-antennas[value][i][1]):
                                    if value not in antinodes:
                                        antinodes[value] = []
                                    antinodes[value].append(position)
                            if (row - antennas[value][i][0]) * (col - antennas[value][j][1]) == (row - antennas[value][j][0]) * (col - antennas[value][i][1]):
                                    if value not in antinodes:
                                        antinodes[value] = []
                                    antinodes[value].append(position)

    uniquenodes = set()
    for value in antinodes:
        for position in antinodes[value]:
            uniquenodes.add(tuple(position))
    sumPart1 = len(uniquenodes)

    print_matrix(uniquenodes, lines)

    print(sumPart1)


startt = time.time()
sumPart1 = 0
part1()
part1time = time.time()-startt
print("time taken part1", part1time )
startt = time.time()
part2()
part2time = time.time()-startt
print("time taken part2", part2time )


