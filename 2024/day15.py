from collections import deque

inputfile  = open('input15.txt').read().splitlines()

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
    G = [list(l) for l in ScaledGraphs]
    spx = startpos[0]
    spy = startpos[1]
    for dir in directions:
        num = 0
        # for l in G:
        #     print(f'{num}',end="")
        #     num += 1
        #     print("".join(l))
        # print("startpos and next direction", spx, dir)
        # if spx == 15 and spy == 52:
        #     print("here")

        G[spx][spy] = '.'

        if dir == '<' and [spx, spy - 1]  not in boundary:
            if G[spx][spy - 1] == '.':
                spx,spy = spx, spy - 1
                G[spx][spy] = '@'
                G[spx][spy+ 1] = '.'
            elif G[spx][spy - 1] == ']':
                for i in range(spy - 1, 0, -1):
                    if G[spx][i] == '#':
                        break
                    if G[spx][i] == '.' :
                        for j in range(i,spy-1):
                            if G[spx][j+1] != '@' or G[spx][j+1] != '.':
                                G[spx][j] = G[spx][j+1]
                        spx,spy = spx, spy - 1
                        G[spx][spy] = '@'
                        G[spx][spy+1] = '.'
                        break
        elif dir == '>' and [spx, (spy) + 1] not in boundary :
            if G[spx][spy + 1] == '.' :
                spx,spy = spx, spy + 1
                G[spx][spy] = '@'
                G[spx][spy -1] = '.'
            elif G[spx][spy + 1] == '[':
                for i in range(spy + 1, len(G[0])):
                    if G[spx][i] == '#' :
                        break
                    if G[spx][i] == '.':
                        for j in range(i,spy+1,-1):
                            G[spx][j] = G[spx][j-1]
                        spx,spy = spx, spy + 1
                        G[spx][spy] = '@'
                        G[spx][spy - 1] = '.'
                        break

        elif dir == '^' and [(spx) - 1, spy] not in boundary:
            if G[spx - 1][spy] == '.':
                spx,spy = spx - 1, spy
                G[spx][spy] = '@'
                G[spx + 1][spy] = '.'
            elif G[spx - 1][spy] == '[' or G[spx - 1][spy] == ']':
                target = deque()
                nextTarget = deque()
                stopMove = False
                placestomove = set()
                placestomoveHalf = set()
                placesnottomovehalf = set()
                spaceforstart = []
                allTargets = []
                if G[spx - 1][spy] == '[':
                    target.append([[spx - 1, spy], [spx - 1, spy + 1]])
                    spaceforstart.append([spx-1, spy+1])
                    allTargets.append([[spx - 1, spy], [spx - 1, spy + 1]])
                elif G[spx - 1][spy] == ']':
                    target.append([[spx - 1, spy - 1], [spx - 1, spy]])
                    allTargets.append([[spx - 1, spy - 1], [spx - 1, spy]])
                    spaceforstart.append([spx-1, spy - 1])
                for i in range(spx - 2, 0, -1):
                    if stopMove:
                        break

                    nextTarget = deque()
                    while target:
                        targets = target.popleft()
                        if G[i][targets[0][1]] == '#' or G[i][targets[1][1]] == '#':
                            stopMove = True
                            break
                        if G[i][targets[0][1]] == '[':
                            nextTarget.append([[i,targets[0][1]],[i,targets[0][1]+1]])
                            allTargets.append([[i,targets[0][1]],[i,targets[0][1]+1]])
                        if G[i][targets[0][1]] == ']':
                            nextTarget.append([[i, targets[0][1]-1], [i, targets[0][1]]])
                            allTargets.append([[i, targets[0][1]-1], [i, targets[0][1]]])
                        if G[i][targets[1][1]] == '[':
                            nextTarget.append([[i, targets[1][1]], [i, targets[1][1] + 1]])
                            allTargets.append([[i, targets[1][1]], [i, targets[1][1] + 1]])
                        if G[i][targets[0][1]] == '.' and G[i][targets[1][1]] == '.':

                            placestomove.add((i, targets[0][1]))
                        elif G[i][targets[0][1]] == '.':

                            placestomoveHalf.add((i, targets[0][1]))
                        elif G[i][targets[1][1]] == '.':

                            placestomoveHalf.add((i, targets[1][1]))
                    target = nextTarget

                if not stopMove and not target:
                    seen = set()
                    deduplicated_list = [x for x in allTargets if not (tuple(map(tuple, x)) in seen or seen.add(tuple(map(tuple, x))))]
                    for [a, b], [c, d] in reversed(deduplicated_list):

                        da, db, dc, dd = a - 1, b, c - 1, d
                        G[da][db] = G[a][b]
                        G[dc][dd] = G[c][d]
                        G[a][b] = '.'
                        G[c][d] = '.'
                    spx, spy = spx - 1, spy
                    G[spaceforstart[0][0]][spaceforstart[0][1]] = '.'




        elif dir == 'v' and [spx + 1, (spy)] not in boundary:
            if G[spx + 1][spy] == '.':
                spx,spy = spx + 1, spy
                G[spx][spy] = '@'
                G[spx - 1][spy] = '.'
            elif G[spx + 1][spy] == '[' or G[spx + 1][spy] == ']':
                target = deque()
                stopMove = False
                placestomove = set()
                placestomoveHalf = set()
                placesnottomovehalf = set()
                allTargets = []
                spaceforstart = []
                if G[spx + 1][spy] == '[' and G[spx + 1][spy + 1] == ']':
                    target.append([[spx + 1, spy], [spx + 1, spy + 1]])
                    spaceforstart.append([spx + 1, spy + 1])
                    allTargets.append([[spx + 1, spy], [spx + 1, spy + 1]])
                elif G[spx + 1][spy] == ']':
                    target.append([[spx + 1, spy - 1], [spx + 1, spy]])
                    spaceforstart.append([spx + 1, spy - 1])
                    allTargets.append([[spx + 1, spy - 1], [spx + 1, spy]])
                for i in range(spx + 2, len(G)):
                    if stopMove:
                        break
                    nextTarget = deque()
                    while target:
                        targets = target.popleft()
                        if G[i][targets[0][1]] == '#' or G[i][targets[1][1]] == '#':
                            stopMove = True
                            break
                        if G[i][targets[0][1]] == '[':
                            nextTarget.append([[i, targets[0][1]], [i, targets[0][1] + 1]])
                            allTargets.append([[i, targets[0][1]], [i, targets[0][1] + 1]])
                        if G[i][targets[0][1]] == ']':
                            nextTarget.append([[i, targets[0][1] - 1], [i, targets[0][1]]])
                            allTargets.append([[i, targets[0][1] - 1], [i, targets[0][1]]])
                        if G[i][targets[1][1]] == '[':
                            nextTarget.append([[i, targets[1][1]], [i, targets[1][1] + 1]])
                            allTargets.append([[i, targets[1][1]], [i, targets[1][1] + 1]])
                        if G[i][targets[0][1]] == '.' and G[i][targets[1][1]] == '.':
                            placestomove.add((i, targets[0][1]))
                        elif G[i][targets[0][1]] == '.':
                            placestomoveHalf.add((i, targets[0][1]))
                        elif G[i][targets[1][1]] == '.':
                            placestomoveHalf.add((i, targets[1][1]))
                    target = nextTarget

                if not stopMove and not target:

                    seen = set()
                    deduplicated_list = [x for x in allTargets if not (tuple(map(tuple, x)) in seen or seen.add(tuple(map(tuple, x))))]
                    for [a,b],[c,d] in reversed(deduplicated_list):
                        da,db,dc,dd = a+1,b,c+1,d
                        # if (da,db) in placestomove:
                        G[da][db] = G[a][b]
                        G[dc][dd] = G[c][d]
                        G[a][b] = '.'
                        G[c][d] = '.'
                        # else:
                    spx, spy = spx + 1, spy
                    G[spaceforstart[0][0]][spaceforstart[0][1]] = '.'
                        #





        else:
            print("Halalalalala")
        G[spx][spy] = '@'
        # for line in G:
        #     print("".join(line))

    result = 0
    for line in G:
        print("".join(line))
    for y in range(len(G)):
        for x in range(len(G[0])):
            if G[y][x] == '[':
                result += ((y*100) + x)
    print (result)

# part1()
part2()
