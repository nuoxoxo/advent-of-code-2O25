D = [(_[0], int(_[1:]))for _ in open(0).read().splitlines()]
r1,i=0,50
r2,j=0,i
for d,n in D:
    lr = 1
    if d == 'L':
        lr = -1
    i += lr*n
    i %= 100
    r1 += (i==0)
    # p2
    for _ in range(n):
        j += lr
        j %= 100
        r2 += (j==0)
print('res1/',r1)
print('res2/',r2)
assert r1 in (3,1123)
assert r2 in (6,6695)
