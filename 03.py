r1,r2=0,0
for a in open(0).read().splitlines():
    N = len(a)
    nums = []
    for l in range(N-1):
        for r in range(l+1,N):
            nums.append(int(a[l]+a[r]))
    #print(max(nums))
    r1+=max(nums)
    # p2
    Q = []
    for i,c in enumerate(a):
        while Q and int(Q[-1]) < int(c) and N-i + len(Q)-1 >= 12:
            Q.pop()
        Q.append(c)
    while len(Q) > 12:
        Q.pop()
    print(''.join(Q))
    r2+=int(''.join(Q))
print(r1,r2)
assert(r2 in (170147128753455,3121910778619))
