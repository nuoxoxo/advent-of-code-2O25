A = [tuple(map(int,_.split(','))) for _ in open(0).read().splitlines()]
N = len(A)
P = []
for i in range(N-1):
    for j in range(i+1,N):
        P.append(((A[i]),(A[j])))
A = []
for p in P:
    ((a,b),(c,d)) = p
    A.append((1+abs(a-c))*(1+abs(b-d)))
print(max(A))#,A)
