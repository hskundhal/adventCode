def part1():
    with open("input7.txt", "r") as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        line = line.strip()
        grid.append(list(line))

    s_idx = set()
    ns_idx = set()
    s_idx.add("".join(grid[0]).find('S', 0))  # str search
    split_counter = 0
    for line in grid[1:]:
        print(line, s_idx)
        while s_idx:
            sdx = s_idx.pop()
            if sdx < 0 or sdx > len(line) - 1:
                continue

            if line[sdx] == '^':
                ns_idx.add(sdx - 1)
                ns_idx.add(sdx + 1)
                split_counter += 1
            elif line[sdx] == '.':
                ns_idx.add(sdx)
        s_idx = ns_idx.copy()  # copy set or list without referring same.
        ns_idx.clear()  # clear set 
    print( split_counter)



def part2():
    with open("input7.txt", "r") as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        line = line.strip()
        grid.append(list(line))
    s_idx = {}
    ns_idx = {}
    start_pos = "".join(grid[0]).find('S',0)
    s_idx[start_pos] = 1 
    result = 0
    split_counter = 0
    for line in grid[1:]:
        # print (line, s_idx) 
        while s_idx:
            sdx, val = s_idx.popitem() 
            if sdx < 0 or sdx >= len(line):
                continue
            
            if line[sdx] == '^':
                ns_idx[sdx-1] = ns_idx.get(sdx-1, 0) + val
                ns_idx[sdx+1] = ns_idx.get(sdx+1, 0) + val
                split_counter += 1
            elif line[sdx] == '.' :
                ns_idx[sdx] = ns_idx.get(sdx, 0) + val

        s_idx = ns_idx.copy() # copy dict
        ns_idx.clear() # clear dict
        
    for val in s_idx.values():
        result += val
    print (result)


print("--- Part 1 ---")
part1()
# 
print("\n--- Part 2 ---")
part2()