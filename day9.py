from collections import deque
import time

def load():
    with open('input9.txt') as f:
        lines = f.read().splitlines()
    return lines

def part1():
    lines = load()

    for line in lines:
        # print(line)
        disk =[]
        place = 0
        value = 0
        for each in line:
            place += 1
            if place %2 == 0:
                for i in range(int(each)):
                    disk.append(".")
            else:
                for i in range(int(each)):
                    disk.append(value)
                value += 1

        # print(disk)
        # print(str(disk))

        disk_lsi = disk
        counter = len(disk_lsi)
        for l in range(len(disk_lsi)):
            print(f'\r{counter}', end="")
            counter -= 1
            if disk_lsi[l] == ".":
                for j in range(len(disk_lsi)-1,l,-1):
                    if disk_lsi[j] != ".":
                        disk_lsi[j],disk_lsi[l] = disk_lsi[l],disk[j]

                        break


        part1sum = 0
        for i in range(len(disk_lsi)):
            if disk_lsi[i] != ".":
                part1sum += i*(int(disk_lsi[i]))
    print ("answer")
    print (part1sum)


def merge(first,second,listdisk):
    if 0<=first<len(listdisk) and 0<=second<len(listdisk):
        if listdisk[first][0] == "." and listdisk[second][0] == ".":
            listdisk[first][1] += listdisk[second][1]
            listdisk.pop(second)
            return True
    return False

def printlistdisk(listdisk):
    for k in range(len(listdisk)):
        print(listdisk[k],k, end=" ")
    print()

def part2():
    lines = load()

    for line in lines:
        # print(line)
        disk = []
        listdisk = []
        place = 0
        value = 0
        for each in line:
            place += 1
            if place % 2 == 0 and each != "0":
                listdisk.append([".", int(each)])
                for i in range(int(each)):
                    disk.append(".")
            else:
                if each != "0":
                    listdisk.append([value, int(each)])
                    for i in range(int(each)):
                        disk.append(value)
                    value += 1

        l1 = 0
        lengthDisk = len(listdisk)
        counter = len(listdisk)
        # while l1 < lengthDisk:


        j = lengthDisk - 1
        while 0< j < lengthDisk:
            print(f'\r{counter}', end="")
            # print(listdisk[j],j,lengthDisk,l1)
            # printlistdisk(listdisk)
            if listdisk[j][0] != "."  and j < lengthDisk:
                for l in range (0, len(listdisk)):
                    # print(listdisk[l],listdisk[j])
                    if listdisk[l][0] == "." and l < j:

                        if listdisk[j][1] <= listdisk[l][1]:
                                # print()
                            # print(f'j={listdisk[j]} l={listdisk[l]}')
                            if listdisk[j][1] == listdisk[l][1]:
                                listdisk[j], listdisk[l] = listdisk[l], listdisk[j]
                                if merge(j,j+1,listdisk):
                                    lengthDisk -= 1
                                if merge(j-1,j,listdisk):
                                    lengthDisk -= 1

                            else:
                                diff = listdisk[l][1] - listdisk[j][1]
                                listdisk[l][1] = listdisk[j][1]
                                listdisk[j], listdisk[l] = listdisk[l], listdisk[j]
                                listdisk.insert(l + 1, [".", diff])
                                lengthDisk += 1
                                j += 1
                                counter += 1
                                if merge(l+1,l+2,listdisk):
                                    lengthDisk -= 1
                                if merge(j+1, j + 2, listdisk):
                                    lengthDisk -= 1
                                if merge(j,j+1,listdisk):
                                    lengthDisk -= 1

                                # printlistdisk(listdisk)
                            break

            l1 += 1
            j -= 1
            counter -= 1

    newstr = ""
    newlistdisk = []
    for k,v in listdisk:
        for i in range(v):
            # print(k,end="")
            newstr+=str(k)
            newlistdisk.append(k)
    # print(newstr)

    part1sum = 0
    for i in range(len(newlistdisk)):
        if newlistdisk[i] != ".":
            part1sum += i * (int(newlistdisk[i]))

    print("answer2:",part1sum)
    print("answer2",part1sum)
    # 85835447779 too low

startt = time.time()
sumPart1 = 0
# part1()
part1time = time.time()-startt
print("time taken part1", part1time )
startt = time.time()
part2()
part2time = time.time()-startt
print("time taken part2", part2time )
