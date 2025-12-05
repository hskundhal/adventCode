lines = open("input5.txt", "r").read().splitlines()

mydict = {
}
series = []
seriesInvalid = []
for line in lines:
    # print(line)
    if line.__contains__("|"):
        x,y = line.split("|")
        # print (x,y,line)
        if mydict.get(x) is None:
            mydict[x] = [y]
        else:
            mydict[x].append(y)
    if line.__contains__(","):
        valid = True
        update = line.split(",")
        # print (update)
        lenUpdate = len(update)-1
        for i in range(0,lenUpdate+1):
            # print(update[i])
            if mydict.get(update[i]) is not None:
                compareWith = mydict.get(update[i])
                if i > 0:
                    for j in range(i-1, 0, -1):
                        for compare in compareWith:
                            if update[j] == compare:
                                valid = False
                                break
            for j in range(i+1, lenUpdate+1):
                # print(update[i], update[j])
                if mydict.get(update[j]) is not None:
                    newCompareWith = mydict.get(update[j])
                    for compare in newCompareWith:
                        if update[i] == compare:
                            valid = False
                            break
        if valid:
            series.append(update)
        else:
            seriesInvalid.append(update)
# print (series)
sum = 0
for item in series:
    # print (item)
    middleitem = int(len(item)/2)
    sum += int(item[middleitem])
    # print (item[middleitem])
print (sum)
# print (mydict)
sum = 0
for item in seriesInvalid:
    print (item)
    lenUpdate = len(item) - 1
    for i in range(0, lenUpdate + 1):
        # print(update[i])
        if mydict.get(item[i]) is not None:
            compareWith = mydict.get(item[i])
            if i > 0:
                for j in range(i - 1, 0, -1):
                    for compare in compareWith:
                        if item[j] == compare:
                            item[i], item[j] = item[j], item[i]
        for j in range(i + 1, lenUpdate + 1):
            # print(update[i], update[j])
            if mydict.get(item[j]) is not None:
                newCompareWith = mydict.get(item[j])
                for compare in newCompareWith:
                    if item[i] == compare:
                        item[i], item[j] = item[j], item[i]

    print (item)
    middleitem = int(len(item) / 2)
    sum += int(item[middleitem])
print(sum)
