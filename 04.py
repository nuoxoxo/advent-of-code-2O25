G = open(0).read().splitlines()
R=len(G)
C=R
S=set()
def ok2(r,c) -> bool:
    res = 0
    D = ((-1,1),(1,-1),(-1,-1),(1,1),(-1,0),(0,1),(0,-1),(1,0))
    for dr,dc in D:
        rr,cc=r+dr,c+dc
        if -1<rr<R and -1<cc<C and (rr,cc) not in S and G[rr][cc]=='@':
            res += 1
    return res < 4
def ok(r,c) -> bool:
    res = 0
    D = ((-1,1),(1,-1),(-1,-1),(1,1),(-1,0),(0,1),(0,-1),(1,0))
    for dr,dc in D:
        rr,cc=r+dr,c+dc
        if -1<rr<R and -1<cc<C and G[rr][cc]=='@':
            res += 1
    return res < 4
r1 = 0    
for r in range(R):
    for c in range(C):
        if G[r][c] == '@' and ok(r,c):
            r1 += 1
yes = True
count = 0
while yes:
    count += 1
    print('it/',count)
    yes = False
    for r in range(R):
        for c in range(C):
            if (r,c) not in S and G[r][c] == '@' and ok2(r,c):
                S.add((r,c))
                yes = True
print(r1,len(S))
