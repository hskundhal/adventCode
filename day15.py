from collections import deque

inputfile  = open('input.txt').read().splitlines()

def part1():
    grid = [list(line) for line in inputfile]
    boundary = []
    directions = []
    startpos = (0,0)
    for y,line in enumerate(inputfile):
        for x,value in enumerate(line):
            if value  == '#':
                boundary.append([y,x])
            if value  in ('v','^','<','>'):
                directions.append(value)
            if value == '@':
                startpos = ([y,x])

    print(boundary)
    print (directions)
    for dir in directions:
        print("startpos",startpos, dir)
        grid[startpos[0]][startpos[1]] = '.'
        if dir == '<' and [startpos[0],(startpos[1])-1]  not in boundary:
            if grid[startpos[0]][startpos[1]-1] == '.':
                print("move left")
                startpos = [startpos[0],(startpos[1])-1]
                grid[startpos[0]][startpos[1]] = '.'
            elif grid[startpos[0]][startpos[1]-1] == 'O':
                for i in range(startpos[1]-1,0,-1):
                    if grid[startpos[0]][i] == '#':
                        break
                    if grid[startpos[0]][i] == '.':
                        print("left",i, (startpos[0],startpos[1]-1))
                        grid[startpos[0]][i] = 'O'
                        startpos = (startpos[0],(startpos[1]-1))
                        grid[startpos[0]][startpos[1]] = '.'
                        break

        elif dir == '^' and [(startpos[0])-1,startpos[1]]  not in boundary:
            if grid[startpos[0] -1][startpos[1]] == '.':
                print("moving up")
                startpos = (startpos[0] - 1, startpos[1])
                grid[startpos[0]][startpos[1]] = '.'
            elif grid[startpos[0] - 1][startpos[1]] == 'O':
                for i in range(startpos[0] - 1, 0, -1):
                    if grid[i][startpos[1]] == '#':
                        break
                    if grid[i][startpos[1]] == '.':
                        print("up", i, (i, startpos[1]))
                        grid[i][startpos[1]] = 'O'
                        startpos = (startpos[0] - 1, (startpos[1]))
                        grid[startpos[0]][startpos[1]] = '.'
                        break
        elif dir == '>' and [startpos[0],(startpos[1])+1]  not in boundary :
            if grid[startpos[0]][startpos[1]+1] == '.':
                print("move right")
                startpos = [startpos[0],(startpos[1])+1]
                grid[startpos[0]][startpos[1]] = '.'
            elif grid[startpos[0]][startpos[1]+1] == 'O':
                for i in range(startpos[1]+1,len(grid[0])):
                    if grid[startpos[0]][i] == '#':
                        break
                    if grid[startpos[0]][i] == '.':
                        print("right1",i, (startpos[0],startpos[1]+1))
                        grid[startpos[0]][i] = 'O'
                        startpos = (startpos[0],(startpos[1]+1))
                        grid[startpos[0]][startpos[1]] = '.'
                        break
        elif dir == 'v' and [startpos[0]+1,(startpos[1])]  not in boundary :
            if grid[startpos[0]+1][startpos[1]] == '.':
                print("moving down")
                startpos = (startpos[0]+1, startpos[1])
                grid[startpos[0]][startpos[1]] = '.'
            elif grid[startpos[0]+1][startpos[1]] == 'O':
                for i in range(startpos[0] + 1, len(grid)):
                    if grid[i][startpos[1]] == '#':
                        break
                    if grid[i][startpos[1]] == '.':
                        print("down", i, (i, startpos[1]))
                        grid[i][startpos[1]]= 'O'
                        startpos = (startpos[0]+1, (startpos[1]))
                        grid[startpos[0]][startpos[1]] = '.'
                        break
        else:
            print("Halalalalala")
        grid[startpos[0]][startpos[1]] = '@'
        # for line in grid:
        #     print("".join(line))

    result = 0
    for line in grid:
        print("".join(line))
    for y in range(len(grid)):
        if grid[y] == []:
            print("empty",y)
            break
        for x in range(len(grid[0])):

            if grid[y][x] == 'O':
                # print(y,x)
                result += ((y*100)+(x))
    print (result)

def part2():
    boundary = []
    directions = []
    ScaledGraphs = []
    startpos = (0, 0)
    for y, line in enumerate(inputfile):
        ScaledGraph = []
        for x, value in enumerate(line):
            if value == '#':
                boundary.append([y, 2*x])
                boundary.append([y, 2*x+1])
                ScaledGraph.append('#')
                ScaledGraph.append('#')
            if value in ('v', '^', '<', '>'):
                directions.append(value)
            if value == '@':
                startpos = ([y, x*2])
                ScaledGraph.append('@')
                ScaledGraph.append('.')
            if value == '.':
                ScaledGraph.append('.')
                ScaledGraph.append('.')
            if value == 'O':
                ScaledGraph.append('[')
                ScaledGraph.append(']')
        if ScaledGraph:
            ScaledGraphs.append(ScaledGraph)

    print(boundary)
    print(directions)

    for line in ScaledGraphs:
        print("".join(line))
    grid = [list(line) for line in ScaledGraphs]
    for dir in directions:

        for line in grid:
            print("".join(line))
        print("startpos", startpos, dir)
        if startpos[0] == 7 and startpos[1] == 11:
            print("catch")
        grid[startpos[0]][startpos[1]] = '.'
        if dir == '<' and [startpos[0], (startpos[1]) - 1]  not in boundary:
            if grid[startpos[0]][startpos[1] - 1] == '.':
                print("move left")
                startpos = [startpos[0], (startpos[1]) - 1]
                grid[startpos[0]][startpos[1]] = '@'
                grid[startpos[0]][startpos[1]+ 1] = '.'
            elif grid[startpos[0]][startpos[1] - 1] == ']':
                for i in range(startpos[1] - 1, 0, -1):
                    if grid[startpos[0]][i] == '#':
                        break
                    if grid[startpos[0]][i] == '.' :
                        print("yo yo left", i, i-1, (startpos[0], startpos[1] ))
                        for j in range(i,startpos[1]-1):
                            if grid[startpos[0]][j+1] != '@' or grid[startpos[0]][j+1] != '.':
                                grid[startpos[0]][j] = grid[startpos[0]][j+1]



                        startpos = (startpos[0], (startpos[1] - 1))
                        grid[startpos[0]][startpos[1]] = '@'
                        grid[startpos[0]][startpos[1]+1] = '.'
                        break


        elif dir == '>' and [startpos[0], (startpos[1]) + 1] not in boundary :
            if grid[startpos[0]][startpos[1] + 1] == '.' :
                print("move right")
                startpos = [startpos[0], (startpos[1]) + 1]
                grid[startpos[0]][startpos[1]] = '@'
                grid[startpos[0]][startpos[1] -1] = '.'
            elif grid[startpos[0]][startpos[1] + 1] == '[':
                for i in range(startpos[1] + 1, len(grid[0])):
                    if grid[startpos[0]][i] == '#' :
                        break
                    if grid[startpos[0]][i] == '.':
                        print(" yo yo right1", i,i+1, (startpos[0], startpos[1]))
                        for j in range(i,startpos[1]+1,-1):

                            grid[startpos[0]][j] = grid[startpos[0]][j-1]

                        startpos = (startpos[0], (startpos[1] + 1))
                        grid[startpos[0]][startpos[1]] = '@'
                        grid[startpos[0]][startpos[1] - 1] = '.'
                        break
        elif dir == '^' and [(startpos[0]) - 1, startpos[1]] not in boundary:
            if grid[startpos[0] - 1][startpos[1]] == '.':
                print("moving up")
                startpos = (startpos[0] - 1, startpos[1])
                grid[startpos[0]][startpos[1]] = '@'
                grid[startpos[0] + 1][startpos[1]] = '.'
            elif grid[startpos[0] - 1][startpos[1]] == '[' or grid[startpos[0] - 1][startpos[1]] == ']':
                target = deque()
                nextTarget = deque()
                stopMove = False
                placestomove = set()
                spaceforstart = []
                if grid[startpos[0] - 1][startpos[1]] == '[':
                    target.append([[startpos[0] - 1, startpos[1]], [startpos[0] - 1, startpos[1] + 1]])
                    spaceforstart.append([startpos[0]-1, startpos[1]+1])
                elif grid[startpos[0] - 1][startpos[1]] == ']':
                    target.append([[startpos[0] - 1, startpos[1] - 1], [startpos[0] - 1, startpos[1]]])
                    spaceforstart.append([startpos[0]-1, startpos[1] - 1])
                for i in range(startpos[0] - 2, 0, -1):
                    if stopMove:
                        break

                    nextTarget = deque()
                    while target:
                        targets = target.popleft()
                        if grid[i][targets[0][1]] == '#' or grid[i][targets[1][1]] == '#':
                            print("cant move up with targets", targets)
                            stopMove = True
                            break
                        if grid[i][targets[0][1]] == '[':
                            nextTarget.append([[i,targets[0][1]],[i,targets[0][1]+1]])
                        if grid[i][targets[0][1]] == ']':
                            nextTarget.append([[i, targets[0][1]-1], [i, targets[0][1]]])
                        if grid[i][targets[1][1]] == '[':
                            nextTarget.append([[i, targets[1][1]], [i, targets[1][1] + 1]])
                        if grid[i][targets[0][1]] == '.' and grid[i][targets[1][1]] == '.':
                            print("target good to be moved", targets, (i, targets[0][1]))
                            placestomove.add((i, targets[0][1]))
                    target = nextTarget

                print("moving these targets up", placestomove)
                if not stopMove:
                    for px,py in placestomove:
                        for j in range(px,startpos[0]-1):
                            if grid[j][py] == '#' or grid[j][py+1] == '#' :
                                break
                            if grid[j+1][py] != '.' :
                                grid[j][py] = grid[j+1][py]
                            if grid[j+1][py+1] != '.':
                                grid[j][py+1] = grid[j+1][py+1]


                    startpos = (startpos[0] - 1, (startpos[1]))
                    grid[startpos[0]][startpos[1]] = '@'
                    grid[spaceforstart[0][0]][spaceforstart[0][1]] = '.'



        elif dir == 'v' and [startpos[0] + 1, (startpos[1])] not in boundary:
            if grid[startpos[0] + 1][startpos[1]] == '.':
                print("moving d")
                startpos = (startpos[0] + 1, startpos[1])
                grid[startpos[0]][startpos[1]] = '@'
                grid[startpos[0] - 1][startpos[1]] = '.'
            elif grid[startpos[0] + 1][startpos[1]] == '[' or grid[startpos[0] + 1][startpos[1]] == ']':
                target = deque()
                nextTarget = deque()
                stopMove = False
                placestomove = set()
                spaceforstart = []
                if grid[startpos[0] + 1][startpos[1]] == '[':
                    target.append([[startpos[0] + 1, startpos[1]], [startpos[0] + 1, startpos[1] + 1]])
                    spaceforstart.append([startpos[0] + 1, startpos[1] + 1])
                elif grid[startpos[0] + 1][startpos[1]] == ']':
                    target.append([[startpos[0] + 1, startpos[1] - 1], [startpos[0] + 1, startpos[1]]])
                    spaceforstart.append([startpos[0] + 1, startpos[1] - 1])
                for i in range(startpos[0] + 2, len(grid)):
                    if stopMove:
                        break

                    nextTarget = deque()
                    while target:
                        targets = target.popleft()
                        if grid[i][targets[0][1]] == '#' or grid[i][targets[1][1]] == '#':
                            print("cant move d with targets", targets)
                            stopMove = True
                            break
                        if grid[i][targets[0][1]] == '[':
                            nextTarget.append([[i, targets[0][1]], [i, targets[0][1] + 1]])
                        if grid[i][targets[0][1]] == ']':
                            nextTarget.append([[i, targets[0][1] - 1], [i, targets[0][1]]])
                        if grid[i][targets[1][1]] == '[':
                            nextTarget.append([[i, targets[1][1]], [i, targets[1][1] + 1]])
                        if grid[i][targets[0][1]] == '.' and grid[i][targets[1][1]] == '.':
                            print("target good to be moved d", targets, (i, targets[0][1]))
                            placestomove.add((i, targets[0][1]))
                    target = nextTarget

                print("moving these targets d", placestomove)
                if not stopMove:
                    for px, py in placestomove:
                        for j in range(px, startpos[0], -1):
                            if grid[j][py] == '#' or grid[j][py + 1] == '#':
                                break
                            # if grid[j][py] != '.' and grid[j][py+1] != '.':
                            grid[j][py] = grid[j - 1][py]
                            # if grid[j][py+1] != '.':
                            grid[j][py + 1] = grid[j - 1][py + 1]

                    startpos = (startpos[0] + 1, (startpos[1]))
                    grid[startpos[0]][startpos[1]] = '@'
                    grid[spaceforstart[0][0]][spaceforstart[0][1]] = '.'



        else:
            print("Halalalalala")
        grid[startpos[0]][startpos[1]] = '@'
        # for line in grid:
        #     print("".join(line))

    result = 0
    for line in grid:
        print("".join(line))
    for y in range(len(grid)):
        if grid[y] == []:
            print("empty", y)
            break
        for x in range(len(grid[0])):

            if grid[y][x] == 'O':
                # print(y,x)
                result += ((y * 100) + (x))
    print(result)

part2()
