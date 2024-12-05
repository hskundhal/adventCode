import re

inputFile = open("input4.txt", "r")
lines = inputFile.read().strip().split("\n")
count = 0
rows = len(lines)
columns = len(lines[0])

print (rows, columns)
patternXMAS = re.compile(r'XMAS')
patternSAMX = re.compile(r'SAMX')
for row in range(rows):
    for column in range(columns):
        # horizontal check
        match = patternXMAS.match(lines[row][column:])
        if match is not None:
            print (row, column, "XMAS")
            count += 1
        # reverse check
        matchR = patternSAMX.match(lines[row][column:])
        if matchR is not None:
            print (row, column, "SAMX")
            count += 1
        # diagnol check
        if lines[row][column] == 'X' :
            # diagonaldownwardforward
            if row+3 < rows:
                if column+3 < columns:
                    if lines[row+1][column+1] == 'M' and lines[row+2][column+2] == 'A' and lines[row+3][column+3] == 'S':
                        count += 1
                        print (row, column, "diagonaldownwardforward")
                # diagonaldownwardbackward
                if  column-3 >= 0:
                    if lines[row+1][column-1] == 'M' and lines[row+2][column-2] == 'A' and lines[row+3][column-3] == 'S':
                        count += 1
                        print (row, column, "diagonaldownwardbackward")
                # vertical check downward
                if lines[row+1][column] == 'M' and lines[row+2][column] == 'A' and lines[row+3][column] == 'S':
                    count += 1
                    print(row,column, "verticaldownward")
        # reverse diagonal check
            if row-3 >= 0:
                # backwarddiagonalforward check
                if column+3 < columns and lines[row-1][column+1] == 'M' and lines[row-2][column+2] == 'A' and lines[row-3][column+3] == 'S':
                    count += 1
                    print(row,column, "backwarddiagonalforward")
                # backwarddiagonalbackward
                if column-3 >= 0 and lines[row-1][column-1] == 'M' and lines[row-2][column-2] == 'A' and lines[row-3][column-3] == 'S':
                    count += 1
                    print(row,column, "backwarddiagonalbackward")
                # vertical check upward
                if lines[row-1][column] == 'M' and lines[row-2][column] == 'A' and lines[row-3][column] == 'S':
                    count += 1
                    print(row,column, "verticalupward")




print(count)
count = 0
for row in range(rows):
    for column in range (columns):

        if row+2 < rows  and column + 2 < columns:
            if lines[row][column] == 'M':
                # diagonal downward forward
                if lines[row+1][column+1] == 'A' and lines[row+2][column+2] =='S':
                    if lines[row+2][column] == 'M' and lines[row+1][column+1] == 'A' and lines[row][column+2] =='S':
                        count += 1
                        # print(row,column, "diagonaldownwardforwardX")
                    if lines[row+2][column] == 'S' and lines[row+1][column+1] == 'A' and lines[row][column+2] =='M':
                        count += 1
                        # print(row,column, "diagonaldownwardforwardX")
            if lines[row][column] == 'S':
                # diagonal downward reverse
                if  lines[row + 1][column + 1] == 'A' and lines[row + 2][column + 2] == 'M':
                    if lines[row + 2][column] == 'M' and lines[row + 1][column + 1] == 'A' and lines[row][column + 2] == 'S':
                        count += 1
                        # print(row, column, "diagonaldownwardrevX")
                    if lines[row + 2][column] == 'S' and lines[row + 1][column + 1] == 'A' and lines[row][column + 2] == 'M':
                        count += 1
                        # print(row, column, "diagonaldownwardrevdX")

print (count)