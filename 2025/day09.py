import itertools


def part1():
    with open("input9.txt", "r") as f:
        lines = f.readlines()
    points = []
    for line in lines:
        line = line.strip()
        points.append(list(map(int,line.split(","))))
    area = 0
    for p1,p2 in itertools.combinations(points,2):
        area = max(area,abs(p1[0]-p2[0]+1)*abs(p1[1]-p2[1]+1))
    print(area)


def part2():
    with open("input9.txt", "r") as f:
        lines = f.readlines()
    points = []
    for line in lines:
        line = line.strip()
        points.append(list(map(int, line.split(","))))
    # print(points)
    points.sort()
    # print(points)
    area_map = {}
    pointsCombo = []
    for p1, p2 in itertools.combinations(points, 2):
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1] )      + 1)
        area_map[tuple(p1),tuple(p2)] = area
        pointsCombo.append((p1,p2))
    sorted_area_map = sorted(area_map.items(),key=lambda x:x[1], reverse=True)
    # print(sorted_area_map)
    # print(pointsCombo)000098 = {tuple: 2} ([1717, 44898], [11168, 21127])

    hor_lines = {}
    ver_lines = {}
    for pc1, pc2 in pointsCombo:
            if pc1[0] == pc2[0]:
                if pc1[1] < pc2[1]:
                    ver_lines.setdefault(pc1[0], []).append(pc1[1])
                    ver_lines.setdefault(pc1[0], []).append(pc2[1])
                else:
                    ver_lines.setdefault(pc1[0], []).append(pc2[1])
                    ver_lines.setdefault(pc1[0], []).append(pc1[1])
            elif pc1[1] == pc2[1]:
                if pc1[0] < pc2[0]:
                    hor_lines.setdefault(pc1[1], []).append(pc1[0])
                    hor_lines.setdefault(pc1[1], []).append(pc2[0])
                else:
                    hor_lines.setdefault(pc1[1], []).append(pc2[0])
                    hor_lines.setdefault(pc1[1], []).append(pc1[0])

    # print(ver_lines)
    # print(hor_lines)
    for x,l in ver_lines.items():
        if (len(set(l))) >2:
            print(x,l, "hye toba")
            break
    mapcount = 1
    sorted_lines = sorted(hor_lines.items(), key=lambda item: item[1][1] - item[1][0], reverse=True)
    # print(sorted_lines)

    total = len(sorted_area_map)
    for p,areaS in sorted_area_map:
        print(f'\r {mapcount} ,{total}', end="")
        # if mapcount == 98:
        #     continue
        p1 = p[0]
        p3 = p[1]
        p2 = (p1[0],p3[1])
        p4 = (p3[0],p1[1])
        # print(p1,p2,p3,p4)

        if checkEdges(p1,p2,p3,p4,ver_lines,hor_lines):
            if p2[1] < p1[1]:
                p1,p2,p3,p4 = p2,p1,p4,p3
            p11 = p1[0]+1,p1[1]+1
            p22 = p2[0]+1,p2[1]-1
            p33 = p3[0]-1,p3[1]-1
            p44 = p4[0]-1,p4[1]+1
            print(p1, p2, p3, p4, areaS)
            if additionalCheckEdges(p11,p22,p33,p44,ver_lines,hor_lines):
                print(p1, p2, p3, p4,areaS)
                break
        mapcount += 1
    # for a in sorted_area_map:
    #     print(a)

def checkEdges(p1,p2,p3,p4,ver_lines,hor_lines):
    if min(p1[1],p2[1]) < 48498 <max(p1[1],p2[1]):
        if 2032 < p1[0] < 94543:
            return False
    if min(p3[1],p4[1]) < 48498 <max(p3[1],p4[1]):
        if 2032 < p3[0] < 94543:
            return False
    if min(p1[1], p2[1]) < 50265 < max(p1[1], p2[1]):
        if 1744 < p1[0] < 94543:
            return False
    if min(p3[1], p4[1]) < 50265 < max(p3[1], p4[1]):
        if 1744 < p3[0] < 94543:
            return False
    # p1 --> p2
    for y in range(min(p1[1],p2[1])+1,max(p1[1],p2[1])):
        if hor_lines.__contains__(y):
            # print(hor_lines[y])
            if p1[0] in range(hor_lines[y][0]+1,hor_lines[y][1]):
                return False
    # p3 --> p4
    for y in range(min(p3[1],p4[1])+1,max(p3[1],p4[1])):
        if hor_lines.__contains__(y):
            # print(hor_lines[y])
            if p3[0] in range(hor_lines[y][0]+1,hor_lines[y][1]):
                return False
    # p1 --> p4
    for x in range(min(p1[0],p4[0])+1,max(p1[0],p4[0])):
        if ver_lines.__contains__(x):
            if p1[1] in range(ver_lines[x][0]+1,ver_lines[x][1]):
                return False
    # p2 --> p3
    for x in range(min(p2[0],p3[0])+1,max(p2[0],p3[0])):
        if ver_lines.__contains__(x):
            if p2[1] in range(ver_lines[x][0]+1,ver_lines[x][1]):
                return False

    return True


def additionalCheckEdges(p1,p2,p3,p4,ver_lines,hor_lines):
    if min(p1[1],p2[1]) <= 48498 <= max(p1[1],p2[1]):
        if 2032 <= p1[0] <= 94543:
            return False
    if min(p3[1],p4[1]) <= 48498 <=max(p3[1],p4[1]):
        if 2032 <= p3[0] <= 94543:
            return False
    if min(p1[1], p2[1]) <= 50265 <= max(p1[1], p2[1]):
        if 1744 <= p1[0] <= 94543:
            return False
    if min(p3[1], p4[1]) <= 50265 <= max(p3[1], p4[1]):
        if 1744 <= p3[0] <= 94543:
            return False
    # p1 --> p2
    for y in range(min(p1[1],p2[1]),max(p1[1],p2[1])+1):
        if hor_lines.__contains__(y):
            # print(hor_lines[y])
            if p1[0] in range(hor_lines[y][0],hor_lines[y][1]+1):
                return False
    # p3 --> p4
    for y in range(min(p3[1],p4[1]),max(p3[1],p4[1])+1):
        if hor_lines.__contains__(y):
            # print(hor_lines[y])
            if p3[0] in range(hor_lines[y][0],hor_lines[y][1]+1):
                return False
    # p1 --> p4
    for x in range(min(p1[0],p4[0]),max(p1[0],p4[0])+1):
        if ver_lines.__contains__(x):
            if p1[1] in range(ver_lines[x][0],ver_lines[x][1]+1):
                return False
    # p2 --> p3
    for x in range(min(p2[0],p3[0]),max(p2[0],p3[0])+1):
        if ver_lines.__contains__(x):
            if p2[1] in range(ver_lines[x][0],ver_lines[x][1]+1):
                return False

    return True



# print("--- Part 1 ---")
# part1()

print("\n--- Part 2 ---")
part2()