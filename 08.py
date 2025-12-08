coors = [list(map(int,_.split(','))) for _ in open(0).read().splitlines()]
D = []
N = len(coors)
for c1 in range(N-1):
    for c2 in range(c1+1,N):
        a,b,c=coors[c1]
        x,y,z=coors[c2]
        dis = (a-x)**2+(b-y)**2+(c-z)**2
        D.append(((a-x)**2+(b-y)**2+(c-z)**2,c1,c2))

# union find
parents = list(range(N))

def find(node):
    # find root
    root = node
    while parents[root] != root:
        root = parents[root]
    # compress path
    while node != root:
        parent = parents[node]
        parents[node] = root
        node = parent
    return root

def u(c1,c2):
    parents[find(c1)] = find(c2)

it = 0
for _,c1,c2 in sorted(D):#[:1000]:
    u(c1,c2)
    if all(find(0) == find(_) for _ in range(N)):
        print('p2/',coors[c1][0]*coors[c2][0],it)
        break
    if it == 999:
        from collections import defaultdict, Counter
        allroots = []
        for node in range(N): allroots.append(find(node))
        a,b,c = sorted(Counter(allroots).values())[-3:]
        print('p1/',a*b*c,it)
    it += 1
