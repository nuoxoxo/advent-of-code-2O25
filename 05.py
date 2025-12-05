R,N = [_.splitlines() for _ in open(0).read().split('\n\n')]
p1 = 0
#S=set()
for n in N:
    n = int(n)
    for rg in R:
        l,r = [int(_) for _ in rg.split('-')]
        #print(n,l,r)
        if n in range(l,r+1):
            p1 += 1
            #print(n,l,r,'yes')
            break
print('p1/',p1)

ranges = []
for rg in R:
    l,r = [int(_) for _ in rg.split('-')]
    ranges.append((l,r))#range(l,r+1))
ranges.sort()
#print(ranges)
L,R=ranges[0]
p2 = R-L+1
L = R
"""
------
    ------
     ^
"""
for l,r in ranges[1:]:
    # print('lr/',l,r)
    # disjoint
    if L < l:
        p2 += r-l+1
        L = r
        #print('disj/',r-l+1)
    # overlapped
    elif L < r:
        p2 += r-L
        #print('over/',r-L)
        L = r

print('p2/',p2)
assert p2 in (360341832208407,14)
assert p1 in (598,3)
