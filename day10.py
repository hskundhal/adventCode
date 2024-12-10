from collections import deque
import time
trailStore = 0
def load():
    arrlines = []
    with open('input10.txt') as f:
        lines = f.read().strip().splitlines()
        for i,line in enumerate(lines):
            arrlines.append([int(x) for x in line])
    return arrlines

def getTrails(x,y,lines,ratingsToo = False):
    visited= set()
    trail = deque()
    score = 0
    trail.append((x,y))
    rows =len(lines)
    cols = len(lines[0])
    while trail:
        r,c = trail.popleft()
        if (r,c) in visited and not ratingsToo:
            continue
        visited.add((r,c))
        if lines[r][c] == 9:
            score += 1
            continue
        for dr,dc in [[0,1],[1,0],[-1,0],[0,-1]]:
            nextr = r+dr
            nextc = c+dc
            if nextr >= 0 and nextc >=0 and nextr < rows and nextc < cols:
                if lines[nextr][nextc] == lines[r][c]+1 and lines[nextr][nextc] <= 9:
                    trail.append((nextr,nextc))
    return score



def part1():
    lines = load()
    # print(lines)
    zerosAt = []
    trailheads = 0
    scores = 0

    # print("len",len(lines))
    for x,row in enumerate(lines):
        for y, col in enumerate(row):
            score = 0
            if col == 0:
                zerosAt.append([x,y])
                score = getTrails(x,y,lines)

            scores += score

    print("trails scores",scores)


def part2():
    lines = load()
    # print(lines)
    zerosAt = []
    trailheads = 0
    trailRatings = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            ratings = 0
            if lines[x][y] == 0:
                zerosAt.append([x,y])
                ratings = getTrails(x,y,lines,True)

            trailRatings += ratings
    print("trails ratings",trailRatings)




startt = time.time()
part1()
part1time = time.time()-startt
print("time taken part1", part1time )
startt = time.time()
part2()
part2time = time.time()-startt
print("time taken part2", part2time )
