D = open(0).read().strip().splitlines()

r1,r2 = 0,0
i = 50
j = i
for line in D:
    d, n = line[0], int(line[1:])
    lr = 1
    if d == 'L':
        lr = -1
    i += n*lr
    i %= 100
    r1 += (i==0)

    # p2
    for _ in range(n):
        j += lr
        j %= 100
        r2 += (j==0)
print('r1/',r1)
print('r2/',r2)

assert r1 in (3,1123)
assert r2 in (6,6695)
