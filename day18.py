from collections import deque

G=[]
rows = 70
cols = 70
sx,sy = 0,0
ey,ex = rows,cols
for r in range(rows+1):
    G.append([])
    for c in range(cols+1):
        G[r].append('.')

def printG():
    for line in G:
        print(''.join(line))

input = open("input18.txt").read().splitlines()

def part1():
    bytes = 1024
    for line in input:
        bytes -= 1
        x,y = [int(x) for x in line.split(',')]
        # print(x,y)
        G[y][x] = '#'
        if bytes == 0:
            break

    scoreArray = []
    sx, sy = 0, 0
    ey, ex = rows, cols

    counti = 0
    SEEN = []
    whattowatch = deque()
    whattowatch.append((sy, sx, counti))
    while whattowatch:
        syi, sxi, counti, = whattowatch.popleft()
        for c, d, e in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            # print(c,d,e)
            count = counti
            dr = syi + c
            dc = sxi + d
            # SEEN = [*SEENi]
            if dr < 0 or dr > rows or dc < 0 or dc > cols:
                continue
            if G[dr][dc] == '#':
                continue
            if (dr, dc, e) in SEEN:
                continue
            else:
                SEEN.append((dr, dc, e))
            count += 1
            if (dr, dc) == (ey, ex):
                # print('reached',count,end)
                scoreArray.append((count))

            whattowatch.append((dr, dc, count))

    if scoreArray:
        score = min(scoreArray)
        print("part1 ans",score)


def part2():
    str = 0
    end = len(input)
    maxused = 0
    end0 = 0
    for n in range(0,end):
        scoreArray = []
        sx, sy = 0, 0
        ey, ex = rows, cols
        for r in range(rows + 1):
            for c in range(cols + 1):
                G[r][c] = '.'
        if end >= len(input) : end = len(input)-1
        for li in range(0, end):
            insx,insy = [int(x) for x in input[li].split(',')]
            # print(insx,insy)
            G[insy][insx] = '#'
        # printG()
        counti = 0
        SEEN = []
        whattowatch = deque()
        whattowatch.append((sy, sx, counti))
        while whattowatch:
            syi,sxi,counti, = whattowatch.popleft()
            for c,d,e in [(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]:
                # print(c,d,e)
                count = counti
                dr = syi+c
                dc = sxi+d
                # SEEN = [*SEENi]
                if dr < 0 or dr > rows or dc < 0 or dc > cols:
                    continue
                if G[dr][dc] == '#':
                    continue
                if  (dr,dc,e) in SEEN:
                    continue
                else:
                    SEEN.append((dr,dc,e))
                count += 1
                if (dr,dc) == (ey,ex):
                    # print('reached',count,end)
                    scoreArray.append((count))

                whattowatch.append((dr,dc,count))
        k = end

        hlf = abs(maxused-end0)//2
        if scoreArray:
            score = max(scoreArray)
        else:
            score = 0
        if maxused == end0 - 1:
            print("first one to make route impossible at line",end0)
            print("values",input[end0-1])
            break
        if score == 0:
            # print("end for last 0", end)
            end0 = end #2885
            end = end//2
            if end < maxused:
                end = maxused
        else:
            end = end + hlf #2913
            maxused = k #2913

part1()
part2()




