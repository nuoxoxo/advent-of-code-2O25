lines = [_.split() for _ in open(0).read().splitlines()]
L,B,J=[],[],[] # lights,btns,jolts
for line in lines:
    temp = []
    for i,_ in enumerate(line[0][1:-1]):
        if _ == '#':
            temp.append(i)
    L.append(set(temp))
    temp = []
    for _ in line[1:-1]:
        temp.append(set([int(presses) for presses in _[1:-1].split(',')]))
    B.append(temp)
    J.append([int(_) for _ in line[-1][1:-1].split(',')]) # p2
#for l in L: print('l/',l)
#for b in B: print('b/',b)
#for j in J: print('j/',j)
p1 = 0
N = len(L)
from itertools import combinations
for i in range(N):
    #print('\nmatch/',L[i],'\nusing/',B[i])
    btn = B[i]
    for presses in range(1,len(btn)+1):
        found = False
        for coms in combinations(btn,r=presses):
            l = set()
            for com in coms:
                l ^= com
            if l == L[i]:
                p1 += presses
                found = True
                break
        if found:
            print('curr/',p1)
            break
print(p1)
