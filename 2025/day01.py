
pos = 50
paswd = 0
prevpos = False
quotient = 0
file = open("input1.txt", "r")
for line in file:
    if pos == 0:
        prevpos = True
    else:
        prevpos = False
    if line.startswith("L"):
        num = int(line[1:])
        paswd += int(num / 100)
        num = num % 100
        pos -= num
        if pos < 0:
            pos += 100
            if not prevpos and pos != 0:
                paswd += 1
    elif line.startswith("R"):
        num = int(line[1:])
        paswd +=  int(num/100)
        num = num % 100
        pos += num
        if pos >= 100:
            pos -= 100
            if not prevpos and pos != 0:
                paswd += 1
    if pos == 0:
        paswd += 1
    print(line, " ", pos, " ", paswd)
file.close()

