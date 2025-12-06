T = open(0).read().splitlines()
def p2():
    A = [_ for _ in T]
    #for a in A:print(a)
    ops = A.pop().split()
    #print(ops)
    R,C=len(A),len(A[0])
    COLS = [0]*C
    for c in range(C):
        for r in range(R):
            #print(A[r][c])
            if A[r][c] == ' ':
                continue
            else:
                COLS[c] = COLS[c] * 10 + int(A[r][c])
        #print(COLS)
    #print(COLS)
    cal = [_ for _ in ops]
    for i in range(len(cal)):
        if cal[i] == '+': cal[i] = 0
        else: cal[i] = 1
    i = 0
    c = 0
    #while True:
    for i in range(len(ops)):
        #print(cal,i,c)
        if ops[i]=='+':
            while c < C and COLS[c] != 0:
                cal[i] += COLS[c]
                c += 1
            if c < C and COLS[c] == 0:
                c += 1
        elif ops[i]=='*':
            while c < C and COLS[c] != 0:
                cal[i] *= COLS[c]
                c += 1
            if c < C and COLS[c] == 0:
                c += 1
    print(sum(cal))
    assert sum(cal) in (7450962489289,3263827)
def p1():
    A = [_ for _ in T]
    A = [_.split() for _ in A]
    ops = A.pop()
    cal = [_ for _ in ops]
    for i in range(len(cal)):
        if cal[i] == '+': cal[i] = 0
        else: cal[i] = 1
    for i,op in enumerate(ops):
        #print(i,op)
        if op == '+':
            #print('+/')
            for j in range(len(A)):
                cal[i] += int(A[j][i])
        else:
            for j in range(len(A)):
                cal[i] *= int(A[j][i])
    #print(cal)
    print(sum(cal))#"""
    assert sum(cal) in (4405895212738,4277556)
p1()
p2()
