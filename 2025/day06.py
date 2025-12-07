def part1():
    with open("input6.txt", "r") as f:
        lines = f.readlines()
    grid=[]
    result = 0
    for line in lines:
        line = line.rstrip('\n')
        line = line.split()
        grid.append(line)

    for i,sign in enumerate(grid[-1]):
        # print(sign , "col" ,i)
        varResult = int(grid[0][i])
        for row in grid[1:-1]:
            varResult = eval(str(varResult)+sign+row[i])
        # print (varResult)
        result += varResult
    print("result ",result)




def part2():
    with open("input6.txt", "r") as f:
        lines = f.readlines()

    detailgrid = []
    result = 0
    for line in lines:
        line = line.rstrip('\n')
        detailgrid.append(list(line))

    transposedetailgrid = [list(row) for row in zip(*detailgrid)]
    
    if transposedetailgrid[0][-1] != " ":
        sign = transposedetailgrid[0][-1]

    startpos = 0
    signResult = int("".join(transposedetailgrid[startpos][:-1]))
    while startpos < len(transposedetailgrid)-1:
        startpos += 1
        if ("".join(transposedetailgrid[startpos])).strip() == "" and startpos < len(transposedetailgrid)-1:
            result = result + signResult
            signResult = int("".join(transposedetailgrid[startpos+1][:-1]))
            if signResult == " ":
                print("haye tooba")
            sign = transposedetailgrid[startpos+1][-1]
            startpos += 2
        if startpos >= len(transposedetailgrid) :
            break

        nextline = "".join(transposedetailgrid[startpos][:-1])
        # print(str(signResult) + sign + nextline, startpos)
        signResult= eval(str(signResult) + sign + nextline)

    print(result+signResult)





print("--- Part 1 ---")
part1()
#
print("\n--- Part 2 ---")
part2()