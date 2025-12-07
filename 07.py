A = open(0).read().splitlines()
G = []
for a in A:
    g = []
    for i in range(len(a)):
        g.append(a[i])
    G.append(g)
R,C = len(G),len(G[0])

# p2
SR,SC = -1,-1
found=False
for r in range(R):
    for c in range(C):
        if G[r][c]=='S':
            SR,SC=r,c
            found = True
            break
    if found:break

dp = [[0]*C for _ in range(R)]
for c in range(C):
    dp[R-1][c] = 1
for r in range(R-2,-1,-1):
    for c in range(C):
        temp = 0
        if G[r+1][c] not in 'S^':
            temp = dp[r+1][c]
        else:
            if c+1<C:
                right = dp[r+1][c+1]# + 1
            if c-1>-1:
                left = dp[r+1][c-1]# + 1
            temp = left+right
        dp[r][c] = temp
print(dp[SR][SC])
#for row in dp: print(row)

# p1
#1467 lo 1538 hi
for r in range(R):
    for c in range(C):
        if G[r][c] in '^':
            if c-1 > -1:
                #G[r+1][c-1]='|' #FIXME
                for rr in range(r+1,R):
                    if G[rr][c-1] != '^':
                        G[rr][c-1] = '|'
                    else:break
            if c+1 < C:
                #G[r+1][c+1]='|'
                for rr in range(r+1,R):
                    if G[rr][c+1] != '^':
                        G[rr][c+1] = '|'
                    else:break
        elif G[r][c] == 'S':
            #G[r+1][c]='|'
            for rr in range(r+1,R):
                if G[rr][c] != '^':
                    G[rr][c] = '|'
                else:break
p1 = 0
#for g in G: print(''.join(g)) #XXX - print and see
for r in range(R):
    for c in range(C):
        p1 += (G[r][c] == '^' and G[r-1][c] == '|')#:
            #p1 += 1
print(p1)
assert p1 in (21,1537)

