
def part1():
    sumInvalidIDs = 0
    with open("input2.txt", "r") as f:
        file = f.readlines()
    for line in file:
        idranges = line.split(',')

    for idrange in idranges:
        print (idrange)
        startRange, endRange = idrange.split('-')
        start = int(startRange)
        end = int(endRange)
        if (len(startRange) == len(endRange)) and len(startRange)%2 == 1 :
            # print(startRange,endRange,"nothing here continue")
            continue
        for i in range(start,end+1):
            stri = str(i)
            if len(stri) %2 == 1:
                # print(i)
                continue

            mid = len(stri)//2
            if stri[:mid] == stri[mid:]:
                sumInvalidIDs += i
                print(stri)
    # part 1
    print(sumInvalidIDs)

def part2():
    sumInvalidIDs = 0
    with open("input2.txt", "r") as f:
        file = f.readlines()
    for line in file:
        idranges = line.split(',')

    for idrange in idranges:
        # print (idrange)
        startRange, endRange = idrange.split('-')
        start = int(startRange)
        end = int(endRange)
        if (len(startRange) == len(endRange)) and len(startRange)%2 == 1 :
            for i in range(start,end+1):
                if i < 10:
                    continue
                stri = str(i)
                good = True
                for digit in stri:
                    if digit != stri[0]:
                        good = False
                        break

                if good :
                    sumInvalidIDs += i
                    print(stri)
                    continue
                mid = len(stri)//2
                for pos in range(1,mid+1):
                # print(stri[:pos+1])
                    divisor = pattern = stri[:pos]
                    n = pos
                    found = False
                    while n <= len(stri):
                        if divisor == stri:
                            # print(stri[:mid],stri[mid:], divisor)
                            # if divisor == stri[:mid]:
                            # print(stri[:mid],stri[mid:], divisor)
                            sumInvalidIDs += i
                            print(stri)
                            found = True
                            break
                        divisor = divisor+pattern
                        n += pos

                    if found :
                        break
            continue

        for i in range(start,end+1):
            if i < 10:
                continue
            stri = str(i)
            leni = len(stri)
            if leni %2 == 1:

                stri = str(i)
                good = True
                for digit in stri:
                    if digit != stri[0]:
                        good = False
                        break

                if good :
                    sumInvalidIDs += i
                    print(stri)
                    continue
                #
                mid = len(stri)//2
                for pos in range(1,mid+1):
                    # print(stri[:pos+1])
                    divisor = pattern = stri[:pos]
                    n = pos
                    found = False
                    while n <= len(stri):
                        if divisor == stri:
                            # print(stri[:mid],stri[mid:], divisor)
                            # if divisor == stri[:mid]:
                            # print(stri[:mid],stri[mid:], divisor)
                            sumInvalidIDs += i
                            print(stri)
                            found = True
                            break
                        divisor = divisor+pattern
                        n += pos

                    if found :
                        break
                continue

            mid = leni//2
            if stri[:mid] == stri[mid:]:
                sumInvalidIDs += i
                print(stri)
                continue
            # print(stri)
            for pos in range(1,mid+1):
                # print(stri[:pos+1])
                divisor = pattern = stri[:pos]
                n = pos
                found = False
                while n <= leni:
                    if divisor == stri:
                        # print(stri[:mid],stri[mid:], divisor)
                        # if divisor == stri[:mid]:
                            # print(stri[:mid],stri[mid:], divisor)
                        sumInvalidIDs += i
                        print(stri)
                        found = True
                        break
                    divisor = divisor+pattern
                    n += pos

                if found :
                    break



    # part 1
    print(sumInvalidIDs)

part1()
part2()








