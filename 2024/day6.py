import os
import time
import timeit
from sys import flags
from time import sleep
import concurrent.futures

def part1():
    lines = open('input6.txt').read().splitlines()
    # print( lines)
    rows = len(lines)
    columns = len(lines[0])
    print( rows, columns)
    mapped = []

    for i in range( rows):
        for j in range( columns):
            if lines[i][j] == '^':
                # print( i, j)
                startpos = (i, j)
                break

    mapped.append(startpos)
    i, j = startpos
    direction = 'up'
    flags = False
    while True:
        k, l, direction,flags = route(i, j, direction, flags, lines, rows, columns)
        if flags:
            break
        if k != i or l != j:
            mapped.append((k, l))
            # print (k,l)
            i, j = k, l
        if k < 0 or k >= rows or l < 0 or l >= columns:
            # print( 'out of bounds')
            break
        line_list = list(lines[k])
        line_list[l] = 'X'
        lines[k] = ''.join(line_list)


    distinctList = list(set(mapped))
    print (distinctList.__len__())

def route( i, j, direction, flags, lines, rows, columns):
    if i < 0 or i >= rows or j < 0 or j >= columns:
        return i, j, direction, True
    if direction == 'up':
        if i-1 >= 0 and lines[i-1][j] != '#':
            return i-1, j, direction, False
        elif i-1 < 0:
            return i, j, 'right', True
        else:
            return i, j, 'right', False
    elif direction == 'down':
        if i+1 < rows and lines[i+1][j] != '#':
            return i+1, j, direction, False
        elif i+1 >= rows:
            return i, j, 'left', True
        else:
            return i, j, 'left', False
    elif direction == 'left':
        if j-1 >= 0 and lines[i][j-1] != '#':
            return i, j-1, direction, False
        elif j-1 < 0:
            return i, j, 'up', True
        else:
            return i, j, 'up', False
    elif direction == 'right':
        if j+1 < columns and lines[i][j+1] != '#':
            return i, j+1, direction, False
        elif j+1 >= columns:
            return i, j, 'down', True
        else:
            return i, j, 'down', False



def check_visited(visited):
    for key in visited:
        if visited[key] >= 2:
            return True
    for key in visited:
        if visited[key] <= 2:
            return False


def simulate_guard(startpos, lines,obsPosX,obsPosY,rows,columns):
    print ( obsPosX, obsPosY)
    print()
    if lines[obsPosX][obsPosY] != '#' and (obsPosX, obsPosY) != startpos:
        copylinesSim = lines[:]
        line_list = list(copylinesSim[obsPosX])
        line_list[obsPosY] = '#'
        copylinesSim[obsPosX] = ''.join(line_list)
        i, j = startpos
        direction = 'up'
        flags = False
        visited = { }
        count = 0
        while True:
            if visited.get((i, j, direction)) is None:
                visited[(i, j,direction)] = 1
            else:
                visited[(i, j,direction)] += 1

            k, l, direction, flags = route(i, j, direction, flags, copylinesSim, rows, columns)
            if flags:
                return 0

            if check_visited(visited):
                return 1
            i, j = k, l
            # line_list = list(lines[i])
            # line_list[j] = 'X'
            # lines[i] = ''.join(line_list)
            # for line in lines:
            #     print(line)
            # print ("-----------------")
    else:
        return 0





def main():
    global loop_positions
    loop_positions = 0

    with open('input6.txt') as f:
        lines = f.read().splitlines()

    rows = len(lines)
    columns = len(lines[0])
    print(rows, columns)


    for i in range(rows):
        for j in range(columns):
            if lines[i][j] == '^':
                startpos = (i, j)
                break
    numCores = os.cpu_count()
    numWorkers = numCores*16
    with concurrent.futures.ThreadPoolExecutor(max_workers=numWorkers) as executor:

        futures = [executor.submit(simulate_guard, startpos,lines,i,j,rows,columns) for i in range(rows) for j in range(columns)]


        results = [future.result() for future in concurrent.futures.as_completed(futures)]


    loop_positions = sum(results)
    print(loop_positions)


if __name__ == "__main__":
    part1()
    main()

