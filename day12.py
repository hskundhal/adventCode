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
    gardenPlots = open('input12.txt').read().splitlines()
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

    for key,values in sameplotdict.items():
        itemall = list(values)
        while values:
            region = []
            value = values.popleft()
            region.append(value)
            values,region,perm = findMatchingplots(value,values,region,4,itemall)
            # print(key, len(region),perm)
            topGarden.append([key,region])
    pricePart2 = 0
    for k,region in topGarden:
        region.sort()
        start  = 0
        sides = set()
        corners = set()
        corner = 0
        notsides = set()
        startQ = deque(region)
        # each = startQ.popleft()
        while startQ:
            each = startQ.popleft()
            eachup = [each[0] - 1,    each[1]]
            eachleft = [each[0],          each[1] - 1]
            eachdown = [each[0] + 1,   each[1]]
            eachright   = [each[0],      each[1] + 1]
            eachleftdown = [each[0] + 1, each[1] - 1]
            eachleftup = [each[0] - 1, each[1] - 1]
            eachrightup = [each[0] - 1, each[1] + 1]
            eachrightdown = [each[0] + 1, each[1] + 1]
            # outside corners
            if (eachleft not in region and eachup not in region):
                corner += 1
                # corners.add((tuple(eachleft), tuple(eachup), tuple(each)))
            if (eachleft not in region and eachdown not in region):
                corner += 1
                # corners.add((tuple(eachleft), tuple(eachdown), tuple(each)))
            if (eachright not in region and eachup not in region):
                corner += 1
                # corners.add((tuple(eachright), tuple(eachup), tuple(each)))
            if (eachright not in region and eachdown not in region):
                corner += 1
                # corners.add((tuple(eachright), tuple(eachdown), tuple(each)))
        #     inside corners

            if (each in region) and (eachleft in region) and (eachdown in region) and (eachleftdown not in region):
                corner += 1
                corners.add((tuple(eachleft), tuple(eachdown), tuple(each)))
            if (each in region) and (eachleft in region) and (eachup in region) and (eachleftup not in region):
                corner += 1
                corners.add((tuple(eachleft), tuple(eachup), tuple(each)))
            if (each in region) and (eachright in region) and (eachdown in region) and (eachrightdown not in region):
                corner += 1
                corners.add((tuple(eachright), tuple(eachdown), tuple(each)))
            if (each in region) and (eachright in region) and (eachup in region) and (eachrightup not in region):
                corner += 1
                corners.add((tuple(eachright), tuple(eachup), tuple(each)))


        # print(k,"area =",len(region), "side=" , corner)
        # print(corners)
        pricePart2 += len(region) * corner
    print("total price ", pricePart2)

# AAAA
# BBCD
# BBCC
# EEEC
# The region containing type A plants has 4 sides, as does each of the regions containing plants of type B, D, and E.
# However, the more complex region containing the plants of type C has 8 sides!

startime = time.time()
part1()
print(f' Time taken {int(time.time()-startime)}s')
startime = time.time()
part2()
print(f' Time taken {int(time.time()-startime)}s')

