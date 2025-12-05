from collections import deque

lines = open('input16.txt').read().splitlines()
G = [list(line) for line in lines]
wall = []
sy,sx,ey,ex = 0,0,0,0
avlspc = []
for y in range(len(G)):
    for x in range(len(G[0])):
        if G[y][x] == '#':
            wall.append((y,x))
        elif G[y][x] == 'S':
            sy,sx = y,x
        elif G[y][x] == 'E':
            ey,ex = y,x
        elif G[y][x] == '.':
            avlspc.append((y,x))
        else:
            print("check Grid setup")

def check_path(whattocheck,scorearray,SEEN):

    while whattocheck:
        a,b,di,scorei = whattocheck.popleft()
        print(f'\r {a} ,{b}', end="")
        for c, d, e in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:

            score =scorei
            # path = pathi.copy()
            # SEE = dict(SEENN)
            nc = a + c
            nd = b + d
            if (nc, nd) in wall:
                continue
            if di == e:
                score += 1
            elif e in ['U', 'D'] and di in ['L', 'R']:
                score += 1001
            elif e in ['L', 'R'] and di in ['U', 'D']:
                score += 1001
            elif di in ['U', 'D'] and e in ['U', 'D']:
                continue
            elif di in ['L', 'R'] and e in ['L', 'R']:
                continue
            if (nc, nd, e) in SEEN:
                if SEEN[(nc,nd,e)] > score:
                    SEEN[(nc,nd,e)]= score
                else:
                    continue
            else:
                SEEN[(nc,nd,e)]= score
            if nc == ey and nd == ex:
                # print(score)
                scorearray.append((score))
            whattocheck.append((nc, nd, e, score))







def part1():

    scoref = 0
    SEEN = {}
    SEbEN = {}
    dir = 'R'
    pathf = 1
    scorearray = []
    path = []
    path.append((sy,sx,dir))
    SEEN[(sy, sx,dir)] = scoref
    SEbEN[(sy, sx, dir)] = scoref
    whattocheck = deque()
    whattocheck.append((sy,sx,dir,scoref))
    check_path(whattocheck,scorearray,SEEN)
    finals = float('inf')
    for (s) in scorearray:
        # print(s,p)
        if s < finals:
            finals = s

    print("answer part1:",finals)
    return finals



best = part1()
# best = 85432

def check_score_path(scorecheck,whattocheck,scorearray,SEEN):

    while whattocheck:
        a,b,di,scorei,SEENN = whattocheck.popleft()
        print(f'\r {a} ,{b}', end="")
        makeitRock = 0
        for c, d, e in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            SEE = SEENN.copy()
            score =scorei
            # path = pathi.copy()
            # SEE = dict(SEENN)
            nc = a + c
            nd = b + d
            if (nc, nd) in wall:
                makeitRock += 1
                if makeitRock == 3:
                    wall.append((nc,nd))
                continue
            if di == e:
                score += 1
            elif e in ['U', 'D'] and di in ['L', 'R']:
                score += 1001
            elif e in ['L', 'R'] and di in ['U', 'D']:
                score += 1001
            elif di in ['U', 'D'] and e in ['U', 'D']:
                continue
            elif di in ['L', 'R'] and e in ['L', 'R']:
                continue
            if (nc, nd, e) in SEEN:
                if SEEN[(nc,nd,e)] < score:
                    continue
                else:
                    SEEN[(nc,nd,e)]= score
            else:
                SEEN[(nc,nd,e)]= score
            if (nc, nd) in SEE:
                    continue
            else:
                SEE[(nc,nd)]= score
            if nc == ey and nd == ex:
                # print(score)
                scorearray.append((score,SEE))
            if score <= scorecheck:
                whattocheck.append((nc, nd, e, score,SEE))



def part2():
    scoref = 0
    SEEN = {}
    SEbEN = {}
    dir = 'R'
    pathf = 1
    scorearray = []
    path = []
    distinctlst = set()
    path.append((sy,sx,dir))
    SEEN[(sy, sx,dir)] = scoref
    SEbEN[(sy, sx, dir)] = scoref
    whattocheck = deque()
    whattocheck.append((sy,sx,dir,scoref,SEbEN))
    check_score_path(best,whattocheck,scorearray,SEEN)
    finals = float('inf')
    for (s,p) in scorearray:
        # print(s,p)
        if s == best:
            for pi in p:
                distinctlst.add(pi)

    print("answer part2:",len(distinctlst))


part2()