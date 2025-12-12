import itertools

import math


def part1():
    with open("input8.txt", "r") as f:
        lines = f.readlines()
    points = []
    for line in lines:
        line = line.strip()
        # print(line)
        x = list(map(int,line.split(",")))
        x = [int(x) for x in line.split(',')]                               #map to int
        
        points.append(x)
    distance_map ={}
    # print(points)
    for p1,p2 in itertools.combinations(points, 2):
        distance_map[tuple(p1),tuple(p2)] = distanceCalc(p1,p2)             #ttypeerror: unhashable type: 'list' 
    # print(distance_map)
    sorted_distance = sorted(distance_map.items(), key=lambda item:item[1])  # sort dict and return list
    # for sd in sorted_distance:
    #     print(sd)
    extensions = 0
    used =[]
    circuits = []
    for points,dis in sorted_distance:
        if extensions < 1000:
            if points[0] not in used and points[1] not in used:
                used.append(points[0])
                used.append(points[1])
                circuits.append(list(points))
                extensions += 1
            elif points[0] in used and points[1] not in used:
                used.append(points[1])
                for circuit in circuits:
                    if points[0] in circuit:
                        circuit.append(points[1])
                        extensions += 1
                        break
            elif points[0] not in used and points[1] in used:
                used.append(points[0])
                for circuit in circuits:
                    if points[1] in circuit:
                        circuit.append(points[0])
                        extensions += 1
                        break
            elif points[0] in used and points[1] in used:
                for circuit in circuits:
                    if points[0] in circuit and points[1] in circuit:
                        extensions += 1
                        break
                    elif points[0] in circuit and points[1] not in circuit:
                        for cir2 in circuits:
                            if points[1] in cir2:
                                
                                circuit.extend(cir2)
                                circuits.remove(cir2)
                                extensions += 1
                                break
                        

    lenCircuits = []
    
    for circuit in circuits:
        print(circuit)
        lenCircuits.append(len(circuit))
    lenCircuits.sort(reverse=True)
    i = 0
    result = 1
    for le in lenCircuits:
        if i < 3:
           result *= le 
        i += 1
    print(result)
    print(lenCircuits)
    
    

    # extensions = 0
    # used = []
    # circuits = points
    # for circuit in circuits:
    #     print(circuit)
    # for points, dis in sorted_distance:
    #     if extensions < 10:
    #         for circuit in circuits:
    #             print(list(points[0]))
    #             if list(points[0]) == circuit:
    #                 circuit.append(points[1])
    #                 extensions += 1
    #                 if points[1] in circuits:
    #                     circuits.remove(points[1])
    #             if list(points[1]) == circuit:
    #                 circuit.append(points[0])
    #                 extensions += 1
    #                 if points[0] in circuits:
    #                     circuits.remove(points[0])
    #        
    # 
    # for circuit in circuits:
    #     print(circuit)




def distanceCalc(point1, point2):
    distance =  math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)
    return distance
        
    

def part2():
    with open("input8.txt", "r") as f:
        lines = f.readlines()
    pointsA = []
    for line in lines:
        line = line.strip()
        # print(line)
        x = list(map(int, line.split(",")))
        x = [int(x) for x in line.split(',')]  # map to int

        pointsA.append(x)
    distance_map = {}
    # print(points)
    for p1, p2 in itertools.combinations(pointsA, 2):
        distance_map[tuple(p1), tuple(p2)] = distanceCalc(p1, p2)  # ttypeerror: unhashable type: 'list' 
    # print(distance_map)
    sorted_distance = sorted(distance_map.items(), key=lambda item: item[1])  # sort dict and return list
    # for sd in sorted_distance:
    #     print(sd)
    extensions = 0
    used = []
    circuits = []
    takeaway = ()
    for points, dis in sorted_distance:
        if extensions < 10000:
            if points[0] not in used and points[1] not in used:
                used.append(points[0])
                used.append(points[1])
                circuits.append(list(points))
                extensions += 1
            elif points[0] in used and points[1] not in used:
                used.append(points[1])
                for circuit in circuits:
                    if points[0] in circuit:
                        circuit.append(points[1])
                        extensions += 1
                        break
            elif points[0] not in used and points[1] in used:
                used.append(points[0])
                for circuit in circuits:
                    if points[1] in circuit:
                        circuit.append(points[0])
                        extensions += 1
                        break
            elif points[0] in used and points[1] in used:
                for circuit in circuits:
                    if points[0] in circuit and points[1] in circuit:
                        extensions += 1
                        break
                    elif points[0] in circuit and points[1] not in circuit:
                        for cir2 in circuits:
                            if points[1] in cir2:
                                circuit.extend(cir2)
                                circuits.remove(cir2)
                                extensions += 1
                                break
            if len(used) == len(pointsA):
                print(circuits)
                print(extensions)
                print("last points", points)
                takeaway = points
                break
 
    result = 1
    result = takeaway[0][0]*takeaway[1][0]
    print(result)


print("--- Part 1 ---")
# part1()
# 
print("\n--- Part 2 ---")
part2()