def part1():
    with open("input6.txt", "r") as f:
        lines = f.readlines()
    grid=[]
    result = 0
    for line in lines:
        line = line.strip()
        line = line.split()
        grid.append(line)

    for i,sign in enumerate(grid[-1]):
        print(sign , "col" ,i)
        varResult = int(grid[0][i])
        for row in grid[1:-1]:
            varResult = eval(str(varResult)+sign+row[i])
        print (varResult)
        result += varResult
    print("result ",result)




def part2():
    with open("input6.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line)


print("--- Part 1 ---")
part1()

# print("\n--- Part 2 ---")
# part2()