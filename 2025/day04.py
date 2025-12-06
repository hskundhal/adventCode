def part1():
    with open("input4.txt","r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line)
    rows = len(lines)
    columns = len (line)
    movables = 0
    for i in range(rows):
        for j in range(columns):
            if lines[i][j] == '@':
                adjspaceCnt = 0
                if i == 0 or i == rows-1:
                    adjspaceCnt += 3
                if j == 0 or j == columns-1 :
                    if i == 0 or i == rows-1:
                        adjspaceCnt += 2
                    else:
                        adjspaceCnt += 3
                if rows-1 > i > 0:
                    if 0 < j < columns-1:
                        if lines[i-1][j-1] == '.':
                            adjspaceCnt += 1
                        if lines[i-1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i-1][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i][j-1] == '.':
                            adjspaceCnt += 1
                        if lines[i][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j-1] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j+1] == '.':
                            adjspaceCnt += 1
                    elif j == 0:
                        if lines[i-1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i-1][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j+1] == '.':
                            adjspaceCnt += 1
                    elif j == columns-1:
                        if lines[i - 1][j - 1] == '.':
                            adjspaceCnt += 1
                        if lines[i - 1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i][j - 1] == '.':
                            adjspaceCnt += 1
                        if lines[i + 1][j - 1] == '.':
                            adjspaceCnt += 1
                        if lines[i + 1][j] == '.':
                            adjspaceCnt += 1
                elif  i == 0:
                    if 0 < j < columns-1:
                        if lines[i][j-1] == '.':
                            adjspaceCnt += 1
                        if lines[i][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j-1] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j+1] == '.':
                            adjspaceCnt += 1
                    elif j == 0:
                        if lines[i][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i+1][j+1] == '.':
                            adjspaceCnt += 1
                    elif j == columns-1:
                        if lines[i][j - 1] == '.':
                            adjspaceCnt += 1
                        if lines[i + 1][j - 1] == '.':
                            adjspaceCnt += 1
                        if lines[i + 1][j] == '.':
                            adjspaceCnt += 1
                elif i == rows - 1:
                    if 0 < j < columns-1:
                        if lines[i-1][j-1] == '.':
                            adjspaceCnt += 1
                        if lines[i-1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i-1][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i][j-1] == '.':
                            adjspaceCnt += 1
                        if lines[i][j+1] == '.':
                            adjspaceCnt += 1
                    elif j == 0:
                        if lines[i-1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i-1][j+1] == '.':
                            adjspaceCnt += 1
                        if lines[i][j+1] == '.':
                            adjspaceCnt += 1
                    elif j == columns-1:
                        if lines[i - 1][j - 1] == '.':
                            adjspaceCnt += 1
                        if lines[i - 1][j] == '.':
                            adjspaceCnt += 1
                        if lines[i][j - 1] == '.':
                            adjspaceCnt += 1

                if adjspaceCnt > 4:
                    movables += 1
    print(movables)

def part2():
    with open("input4.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line)
    rows = len(lines)
    columns = len(line)
    movables = 0
    movablethisloop = 1

    while movablethisloop > 0:
        movablethisloop = 0
        newlines = [[0 for x in range(columns)] for y in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if lines[i][j] == '@':
                    adjspaceCnt = 0
                    if i == 0 or i == rows - 1:
                        adjspaceCnt += 3
                    if j == 0 or j == columns - 1:
                        if i == 0 or i == rows - 1:
                            adjspaceCnt += 2
                        else:
                            adjspaceCnt += 3
                    if rows - 1 > i > 0:
                        if 0 < j < columns - 1:
                            if lines[i - 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j + 1] == '.':
                                adjspaceCnt += 1
                        elif j == 0:
                            if lines[i - 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j + 1] == '.':
                                adjspaceCnt += 1
                        elif j == columns - 1:
                            if lines[i - 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j] == '.':
                                adjspaceCnt += 1
                    elif i == 0:
                        if 0 < j < columns - 1:
                            if lines[i][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j + 1] == '.':
                                adjspaceCnt += 1
                        elif j == 0:
                            if lines[i][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j + 1] == '.':
                                adjspaceCnt += 1
                        elif j == columns - 1:
                            if lines[i][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i + 1][j] == '.':
                                adjspaceCnt += 1
                    elif i == rows - 1:
                        if 0 < j < columns - 1:
                            if lines[i - 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i][j + 1] == '.':
                                adjspaceCnt += 1
                        elif j == 0:
                            if lines[i - 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j + 1] == '.':
                                adjspaceCnt += 1
                            if lines[i][j + 1] == '.':
                                adjspaceCnt += 1
                        elif j == columns - 1:
                            if lines[i - 1][j - 1] == '.':
                                adjspaceCnt += 1
                            if lines[i - 1][j] == '.':
                                adjspaceCnt += 1
                            if lines[i][j - 1] == '.':
                                adjspaceCnt += 1

                    if adjspaceCnt > 4:
                        movablethisloop += 1
                        newlines[i][j] = '.'
                    else:
                        newlines[i][j] = lines[i][j]
                else:
                    newlines[i][j] = lines[i][j]
        lines = newlines
        movables += movablethisloop
    print(movables)


part1()
part2()