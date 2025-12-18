import itertools
import re
with open("input10.txt","r") as f:
    lines = f.readlines()
# print(lines)
result = 0
for line in lines:
    line = line.strip()
    match = re.match(r'\[(.*)] (.*) {(.*)}', line)
    lights,buttonstr,c = match.groups()
    # print(lights,buttonstr,c)
    initLights = [0]* len(lights)
    # print(initLights)
    lightsOn = [1 if c == '#' else 0 for c in lights]
    # print(lightsOn)
    buttoncombo = 1
    buttons = []
    buttonNew = buttonstr.split(" ")
    for each in buttonNew:
        each = str(each).strip("()").split(",")
        buttons.append([int(x) for x in each])
    # print(buttons)
    notout = True
    for k in range(1,len(buttons)):
        if notout:
            for combos in itertools.combinations(buttons,k):
                # print(combos)
                lightc = initLights.copy()
                for button in combos:
                    for lightindex in button:
                        lightc[int(lightindex)] ^= 1
                if lightc == lightsOn:
                    print(lightc, k)
                    result += k
                    notout = False
                    break

print(result)

