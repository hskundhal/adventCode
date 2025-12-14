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
    for line in lines:
        line = line.strip()
        print(line)


print("--- Part 1 ---")
part1()

# print("\n--- Part 2 ---")
# part2()