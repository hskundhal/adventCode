import math
import time

lines = open('input.txt').read().splitlines()

def part1():
    allitems = []
    winnerPlatter = []
    for i, line in enumerate(lines):
        rotateNew = i % 3 == 0

        key = line.split(':')[0]

        if key != '':
            value = (line.split(':')[1])
            valuesplit = value.split(',')
            xadditions = valuesplit[0].split('+')
            yadditions = valuesplit[1].split('+')

            if key == 'Prize':
                xprize = valuesplit[0].split('=')
                yprize = valuesplit[1].split('=')
                winnerPlatter.append([xprize[1], yprize[1]])
                allitems.append(winnerPlatter)
                winnerPlatter = []

            else:
                winnerPlatter.append([xadditions[1], yadditions[1]])

    # print(allitems)
    # these machines have two buttons labeled A and B. Worse, you can't just put in a token and play; it costs 3 tokens to push the A button and 1 token to push the B button.
    # Pushing the machine's A button would move the claw 94 units along the X axis and 34 units along the Y axis.
    # Pushing the B button would move the claw 22 units along the X axis and 67 units along the Y axis.
    # The prize is located at X=8400, Y=5400; this means that from the claw's initial position, it would need to move exactly 8400 units along the X axis and exactly 5400 units along the Y axis to be perfectly aligned with the prize in this machine.
    # The cheapest way to win the prize is by pushing the A button 80 times and the B button 40 times. This would line up the claw along the X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 280 tokens.
    totalCost = 0
    totalitems = len(allitems)
    for item in allitems:
        print(f'\r {totalitems}',end = "")
        totalitems -= 1
        price = float('inf')
        for i in range(0, len(item)):
            if i == 0:
                x1 = int(item[i][0])
                y1 = int(item[i][1])
            elif i == 1:
                x2 = int(item[i][0])
                y2 = int(item[i][1])
            else :
                x3 = int(item[i][0])
                y3 = int(item[i][1])

        for i in range(max(x3//x1,y3//y1)):
            for j in range(max(x3//x2,y3//y2)):
                if x1*i+x2*j == x3 and y1*i+y2*j == y3:
                    priceIteration = i*3+j*1
                    if priceIteration < price:
                        price = priceIteration
        if price < float('inf'):
            totalCost += price
    print(" totalcost =",totalCost)



def part2():
    allitems = []
    winnerPlatter = []
    for i, line in enumerate(lines):
        rotateNew = i % 3 == 0

        key = line.split(':')[0]

        if key != '':
            value = (line.split(':')[1])
            valuesplit = value.split(',')
            xadditions = valuesplit[0].split('+')
            yadditions = valuesplit[1].split('+')

            if key == 'Prize':
                xprize = valuesplit[0].split('=')
                yprize = valuesplit[1].split('=')
                winnerPlatter.append([xprize[1], yprize[1]])
                allitems.append(winnerPlatter)
                winnerPlatter = []

            else:
                winnerPlatter.append([xadditions[1], yadditions[1]])

    totalCost = 0
    totalitems = len(allitems)
    for item in allitems:
        print(f'\r {totalitems}', end="")
        totalitems -= 1
        price = float('inf')
        for i in range(0, len(item)):
            if i == 0:
                x1 = int(item[i][0])
                y1 = int(item[i][1])
            elif i == 1:
                x2 = int(item[i][0])
                y2 = int(item[i][1])
            else:
                x3 = int(item[i][0])
                y3 = int(item[i][1])

        for i in range(max(x3 // x1, y3 // y1)):
            for j in range(max(x3 // x2, y3 // y2)):
                if x1 * i + x2 * j == x3 and y1 * i + y2 * j == y3:
                    priceIteration = i * 3 + j * 1
                    if priceIteration < price:
                        price = priceIteration
        if price < float('inf'):
            totalCost += price
    print(" totalcost =", totalCost)



startime = time.time()
part1()
print(f' Time taken {int(time.time()-startime)}s')
startime = time.time()
# part2()
