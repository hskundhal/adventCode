import time
from collections import deque


inputfile = open('input14.txt').read().splitlines()

def printAllpos(allpos,rows=7,cols=11):
    for y in range(rows):
        for x in range(cols):
            if (x,y) in allpos:
                print("*",end="")
            else:
                print(".",end="")
        print()


def quadSafetyCount(newpos,verticalcol,horizontalrow):
    quadcount = [0, 0, 0, 0]
    for i in range(4):
        for p in newpos:
            if i == 0:
                if p[0] < verticalcol and p[1] < horizontalrow:
                    quadcount[i] += 1
            if i == 1:
                if p[0] > verticalcol and p[1] < horizontalrow:
                    quadcount[i] += 1
            if i == 2:
                if p[0] < verticalcol and p[1] > horizontalrow:
                    quadcount[i] += 1
            if i == 3:
                if p[0] > verticalcol and p[1] > horizontalrow:
                    quadcount[i] += 1
    result = 1
    for each in quadcount:
        result *= each
    return result

def part1(secondsAfter = 100):
    allpos = []
    allposvel = []
    for line in inputfile:
        posvel =line.split(" ")
        pos = tuple(map(int, posvel[0].split("=")[1].split(",")))
        allpos.append(pos)
        vel = tuple(map(int,posvel[1].split("=")[1].split(",")))
        allposvel.append([pos,vel])

    allpos.sort()
    allposvel.sort()

    rows = 103
    cols = 101
    newpos = []
    for i in range(secondsAfter):
        newposvel = []
        newpos = []
        for p,v in allposvel:
            z0=p[0]+v[0]
            z1=p[1]+v[1]
            if z1 < 0:
                z1 = rows + z1
            if z1 >= rows:
                z1 = z1 - rows
            if z0 < 0:
                z0 = cols +z0
            if z0 >= cols:
                z0 = z0 - cols
            z = (z0,z1)
            newposvel.append([z,v])
            newpos.append(z)
        allposvel = newposvel
        # print("after ", secondsAfter, " seconds")
        # printAllpos(newpos, rows, cols)
    verticalcol =  cols//2 + 1 -1
    horizontalrow = rows//2 + 1 -1
    ans = quadSafetyCount(newpos,verticalcol,horizontalrow)
    print("part1 answer :",ans)

    return ans

def part2( secondsAfter = 10000):
    allpos = []
    allposvel = []
    for line in inputfile:
        posvel = line.split(" ")
        pos = tuple(map(int, posvel[0].split("=")[1].split(",")))
        allpos.append(pos)
        vel = tuple(map(int, posvel[1].split("=")[1].split(",")))
        allposvel.append([pos, vel])

    allpos.sort()
    allposvel.sort()
    rows = 103
    cols = 101
    verticalcol = cols // 2 + 1 - 1
    horizontalrow = rows // 2 + 1 - 1
    minans = float('inf')
    timefomin = 0
    clustermax = 1
    for i in range(secondsAfter):
        newposvel = []
        newpos = []
        flag = False
        for p, v in allposvel:
            z0 = p[0] + v[0]
            z1 = p[1] + v[1]
            if z1 < 0:
                z1 = rows + z1
            if z1 >= rows:
                z1 = z1 - rows
            if z0 < 0:
                z0 = cols + z0
            if z0 >= cols:
                z0 = z0 - cols
            z = (z0, z1)
            # if z in newpos:
            #     newpos = []
            #     flag = False
            #     break
            newposvel.append([z, v])
            newpos.append(z)
        allposvel = newposvel

        # count groups
        newpos.sort()
        newposQ = deque(newpos)
        cluster = 0
        while newposQ:
            each = newposQ.popleft()
            # x,y are mismatched to y and x but should not matter
            eachup = [each[0] - 1, each[1]]
            eachleft = [each[0], each[1] - 1]
            eachdown = [each[0] + 1, each[1]]
            eachright = [each[0], each[1] + 1]
            eachleftdown = [each[0] + 1, each[1] - 1]
            eachleftup = [each[0] - 1, each[1] - 1]
            eachrightup = [each[0] - 1, each[1] + 1]
            eachrightdown = [each[0] + 1, each[1] + 1]
            if tuple(each) in newposQ:
                newposQ.remove(each)
            if tuple(eachup) in newposQ:
                cluster += 1
            if  tuple(eachleft) in newposQ:
                cluster += 1
            if  tuple(eachdown) in newposQ:
                cluster += 1
            if  tuple(eachright)in newposQ:
                cluster += 1
            if  tuple(eachleftdown) in newposQ:
                cluster += 1
            if  tuple(eachleftup) in newposQ:
                cluster += 1
            if  tuple(eachrightup) in newposQ:
                cluster += 1
            if  tuple(eachrightdown) in newposQ:
                cluster += 1

        if cluster > clustermax and cluster > 233:
            clustermax = cluster
            timefomin = i
            flag = True
            print("after ", timefomin, " seconds" , " and cluster size", cluster)

        print(f'\rafter { i}  seconds {("*" * (i//100))}', end="")

        if flag:
            printAllpos(newpos, rows, cols)


        # ans = quadSafetyCount(newpos, verticalcol, horizontalrow)
        # print(ans)
        # if ans < minans:
        #     minans = ans
        #     timefomin = i
    # print("minans",minans , "at secs", timefomin)
#     8257 sec is the time with min safety count but grid doesnt look anuthing like christmas
# no overlap starts at 3 sec so no good


starttime = time.time()
print(part1())
print("time taken", time.time()-starttime)
print()
print("part 2 *******************************************")
starttime = time.time()
print(part2())
print("time taken", time.time()-starttime)


