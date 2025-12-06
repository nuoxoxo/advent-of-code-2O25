LINES = open(0).read().splitlines()
def p2():
    A = [_ for _ in LINES]
    ops = A.pop().split()
    R,C=len(A),len(A[0])
    COLS = [0]*C
    for c in range(C):
        for r in range(R):
            if A[r][c] != ' ':
                COLS[c] = COLS[c] * 10 + int(A[r][c])
    res = [0 if op=='+' else 1 for op in ops]
    i = 0
    c = 0
    for i in range(len(ops)):
        if ops[i] == '+':
            while c < C and COLS[c] != 0:
                res[i] += COLS[c]
                c += 1
            if c < C and COLS[c] == 0:
                c += 1
        elif ops[i] == '*':
            while c < C and COLS[c] != 0:
                res[i] *= COLS[c]
                c += 1
            if c < C and COLS[c] == 0:
                c += 1
    print(sum(res))
    assert sum(res) in (7450962489289,3263827)

def p1():
    A = [_.split() for _ in LINES]
    ops = A.pop()
    res = [0 if op=='+' else 1 for op in ops]
    for i,op in enumerate(ops):
        if op == '+':
            for j in range(len(A)): res[i] += int(A[j][i])
        else:
            for j in range(len(A)): res[i] *= int(A[j][i])
    print(sum(res))
    assert sum(res) in (4405895212738,4277556)

p1()
p2()
