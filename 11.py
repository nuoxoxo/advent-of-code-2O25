A = [_.split(':') for _ in open(0).read().splitlines()]
from collections import defaultdict#,deque
from functools import cache
D = defaultdict(list)
for l,r in A:
    r = r.split()
    for word in r:
        D[l].append(word)

def p1():
    Q = [('you',1)]
    res = 0
    while Q:
        node,n = Q.pop()
        if node == 'out':
            res += n
        else:
            for nxt in D[node]:
                Q.append((nxt,n))
    return res
#w1,w2='dac','fft'
@cache
def p2(node,dac,fft):
    if node == 'out':
        if dac and fft:
            return 1
        return 0
    temp = 0
    for nx in D[node]:
        temp += p2(nx,dac or nx == 'dac',fft or nx == 'fft')
    return temp

print(p1())
print(p2('svr',False,False) )
