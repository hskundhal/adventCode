

def part1():
    with open("input5.txt", "r") as f:
        lines = f.readlines()
    ranges = []
    ingredients = []
    fresh = 0
    ingredientsStarted = False
    for line in lines:
        line = line.strip()
        # print(line)
        if line != "" and not ingredientsStarted:
            ranges.append(line)
        elif line == "":
            ingredientsStarted = True
            continue
        if ingredientsStarted:
            ingredients.append(line)
    # print(ranges)
    # print(ingredients)
    for ingredient in ingredients:
        for range in ranges:
            l,h = range.split("-")
            if int(l)<=int(ingredient)<=int(h):
                # print(ingredient)
                fresh +=1
                break
    print(fresh)


def part2():
    with open("input5.txt", "r") as f:
        lines = f.readlines()
    ranges = []
    mergedRanges = []
    finalmergedRanges = []
    # freshset = set() # empty set is defined else {} creates dict
    ingredientCount = 0
    ingredientsStarted = False
    for line in lines:
        line = line.strip()
        # print(line)
        if line != "" and not ingredientsStarted:
            ranges.append(line)
        elif line == "":
            ingredientsStarted = True
            continue

    for r in ranges:
        l,h = map(int,r.split("-"))
        mergedRanges.append([l,h]) # tuples here will be immutable
    mergedRanges.sort(key= lambda x : x[0])
    for i, mr in enumerate(mergedRanges):
        if i == 0:
            finalmergedRanges.append(mr)
            continue
        else:
            if mr[0] <= finalmergedRanges[-1][1] : # = makes merge for same numbers else counts get off
                if mr[1] > finalmergedRanges[-1][1]:
                    finalmergedRanges[-1][1] = mr[1]
            else:
                finalmergedRanges.append(mr)
    # print(finalmergedRanges)
    for l,h in finalmergedRanges:
        print (l,h)
        ingredientCount = ingredientCount + h - l +1
    print(ingredientCount)




print("--- Part 1 ---")
part1()

print("\n--- Part 2 ---")
part2()