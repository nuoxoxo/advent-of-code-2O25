r1,r2 = 0,0
for a in [_.split('-') for _ in open(0).read().strip().split(',')]:
    l,r = [int(_)for _ in a]
    for n in range(l,r+1):
        s = str(n)
        L = len(s)
        if L%2==0 and s[:L//2]==s[L//2:]:
            r1 += n
        # p2
        if s in (s+s)[1:-1]:
            r2 += n
print(r1,r2)
assert r1 in (1227775554,55916882972)
assert r2 in (4174379265,76169125915)
