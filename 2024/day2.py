inputfile = open("input2.txt", "r")
reports = inputfile.read().strip().split("\n")

def check_level(levels):
    slide = 0
    for i in range(len(levels)-1):
        left, right = int(levels[i]), int(levels[i+1])
        # print (i, left, right)
        if left == right:
            print("found same level", left, right)
            return False
        if left < right and slide != 2:
            slide = 1
            # print("up")
        elif left > right and slide != 1:
            slide = 2
            # print("down")
        else:
            print("slope change", left, right)
            return False

        if abs(right - left) > 3:
            print("no good", left, right)
            return False
    return True

correctLevels = 0
newCorrectReports = 0
for report in reports:
    levels = report.split()
    if check_level(levels):
        print("YES" , levels)
        correctLevels += 1

    for level in range(len(levels)):
        newlevels = levels[:level] + levels[level+1:]
        print(levels, " -> ", newlevels)
        if check_level(newlevels):
            print("YES" , newlevels)
            newCorrectReports += 1
            break
print("Correct levels: ")
print(correctLevels)
print("Correct new reports: ")
print(newCorrectReports)
