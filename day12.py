from collections import deque
import time
from turtledemo.sorting_animate import start_qsort


def part1():
    gardenPlots = open('input12.txt').read().splitlines()

    # This 4x4 arrangement includes garden plots growing five different types of plants (labeled A, B, C, D, and E), each grouped into their own region.
    # In order to accurately calculate the cost of the fence around a single region, you need to know that region's area and perimeter.
    # The area of a region is simply the number of garden plots the region contains. The above map's type A, B, and C plants are each in a region of area 4. The type E plants are in a region of area 3; the type D plants are in a region of area 1.
    # Each garden plot is a square and so has four sides. The perimeter of a region is the number of sides of garden plots in the region that do not touch another garden plot in the same region. The type A and C plants are each in a region with perimeter 10. The type B and E plants are each in a region with perimeter 8. The lone D plot forms its own region with perimeter 4.

    sameplotdict = {}
    checkThis = 0
    totalRows = len(gardenPlots)
    for x,gardenPlotRow in enumerate(gardenPlots):
        for y,gardenPlot in enumerate(gardenPlotRow):
            if sameplotdict.get(gardenPlot) == None:
                sameplotdict[gardenPlot] = deque()
            sameplotdict[gardenPlot].append([x,y])
        flagOfContinuity = True
    print()

    # 's type A, B, and C plants are each in a region of area 4. The type E plants are in a region of area 3; the type D plants are in a region of area 1.
    # The type A and C plants are each in a region with perimeter 10. The type B and E plants are each in a region with perimeter 8. The lone D plot forms its own region with perimeter 4.
    topGarden = []

    def findMatchingplots(value,values,region,sidematchforPerimeter,itemall):
        if not values:
            return values,region,sidematchforPerimeter
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            value2 = [value[0] + dr, value[1] + dc]
            if value2 in itemall:
                sidematchforPerimeter -= 1
                if gardenPlots[value[0]][value[1]] == gardenPlots[value2[0]][value2[1]] and value2 in values:
                    values.remove(value2)
                    region.append(value2)
                    if values:
                        sidematchforPerimeterfromLoop = 4
                        values, region, sidematchforPerimeterfromLoop = findMatchingplots(value2, values, region,sidematchforPerimeterfromLoop, itemall)
                        sidematchforPerimeter += sidematchforPerimeterfromLoop
                    else:
                        lastside =4
                        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            valuelast = [value2[0] + dr, value2[1] + dc]
                            if valuelast in itemall:
                                lastside -= 1
                        sidematchforPerimeter += lastside


        return values,region,sidematchforPerimeter
    # In the first example, region A has price 4 * 10 = 40, region B has price 4 * 8 = 32, region C has price 4 * 10 = 40, region D has price 1 * 4 = 4, and region E has price 3 * 8 = 24. So, the total price for the first example is 140
    priceRegion = 0
    for key,values in sameplotdict.items():
        itemall = list(values)
        while values:
            region = []
            value = values.popleft()
            region.append(value)
            values,region,perm = findMatchingplots(value,values,region,4,itemall)
            # print(key, len(region),perm)
            priceRegion += len(region) * perm
            topGarden.append([region,perm])
    print("total price ",priceRegion)

def part2():
    gardenPlots = open('input.txt').read().splitlines()
    sameplotdict = {}
    for x,gardenPlotRow in enumerate(gardenPlots):
        for y,gardenPlot in enumerate(gardenPlotRow):
            if sameplotdict.get(gardenPlot) == None:
                sameplotdict[gardenPlot] = deque()
            sameplotdict[gardenPlot].append([x,y])
    # print(sameplotdict)
    topGarden = []


    def findMatchingplots(value,values,region,sidematchforPerimeter,itemall):
        if not values:
            return values,region,sidematchforPerimeter
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            value2 = [value[0] + dr, value[1] + dc]
            if value2 in itemall:
                sidematchforPerimeter -= 1
                if gardenPlots[value[0]][value[1]] == gardenPlots[value2[0]][value2[1]] and value2 in values:
                    values.remove(value2)
                    region.append(value2)
                    if values:
                        sidematchforPerimeterfromLoop = 4
                        values, region, sidematchforPerimeterfromLoop = findMatchingplots(value2, values, region,sidematchforPerimeterfromLoop, itemall)
                        sidematchforPerimeter += sidematchforPerimeterfromLoop
                    else:
                        lastside =4
                        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            valuelast = [value2[0] + dr, value2[1] + dc]
                            if valuelast in itemall:
                                lastside -= 1
                        sidematchforPerimeter += lastside


        return values,region,sidematchforPerimeter
    # # In the first example, region A has price 4 * 10 = 40, region B has price 4 * 8 = 32, region C has price 4 * 10 = 40, region D has price 1 * 4 = 4, and region E has price 3 * 8 = 24. So, the total price for the first example is 140
    priceRegion = 0
    for key,values in sameplotdict.items():
        itemall = list(values)
        while values:
            region = []
            value = values.popleft()
            region.append(value)
            values,region,perm = findMatchingplots(value,values,region,4,itemall)
            # print(key, len(region),perm)
            priceRegion += len(region) * perm
            topGarden.append([key,region])
    print("total price ",priceRegion)
    for k,region in topGarden:
        region.sort()
        start  = 0
        sides = set()
        notsides = set()
        startQ = deque(region)
        # each = startQ.popleft()
        while startQ:
            each = startQ.popleft()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                each3 = [each[0] + dr, each[1] + dc]
                if each3 in region :
                    # if each3 in startQ:
                        # startQ.remove(each3)
                    # if dr == 0:
                    #     sides.add((each[0],0))
                    # elif dc == 0:
                    #     sides.add((0,each[1]))
                    continue
                else:
                    start += 1
                    sides.add((each3[0], each3[1]))


        print(k,len(region), len(sides), len(notsides))
        print(sides)


# A region of R  10 = 120.
# A region of I  4 = 16.
# A region of I  16 = 224
# A region of C  22 = 308.
# A region of F plants with price 10 * 12 = 120.
# A region of V plants with price 13 * 10 = 130.
# A region of J plants with price 11 * 12 = 132.
# A region of C plants with price 1 * 4 = 4.
# A region of E plants with price 13 * 8 = 104.

# A region of M plants with price 5 * 6 = 30.
# A region of S plants with price 3 * 6 = 18.
startime = time.time()
part1()
print(f' Time taken {int(time.time()-startime)}s')
# startime = time.time()
# part2()

