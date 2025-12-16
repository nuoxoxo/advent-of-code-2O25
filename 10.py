lines = [_.split() for _ in open(0).read().splitlines()]
L,B,J=[],[],[] # lights,btns,jolts
for line in lines:
    temp = []
    for i,_ in enumerate(line[0][1:-1]):
        if _ == '#':
            temp.append(i)
    L.append(set(temp))
    b = []
    for _ in line[1:-1]:
        b.append(set([int(presses) for presses in _[1:-1].split(',')]))
    B.append(b)
    J.append([int(_) for _ in line[-1][1:-1].split(',')]) # p2

import z3
p2 = 0
N = len(L)
for i in range(N):
    V = z3.Ints([f'v{n}' for n in range(len(B[i]))])# ]
    O = z3.Optimize()
    for v in V:
        O.add(v >= 0)
    for t,target in enumerate(J[i]):
        terms = []
        for b,button in enumerate(B[i]):
            if t in button:
                terms.append(V[b])
        O.add( sum(terms) == target )
    O.minimize(sum(V))
    assert O.check()
    M = O.model()
    p2 += sum( M[v].as_long() for v in V )
print('p2/',p2)

p1 = 0
N = len(L)
from itertools import combinations
for i in range(N):
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
            break
print('p1/',p1)

