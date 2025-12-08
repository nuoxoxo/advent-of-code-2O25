res1,res2=0,0
for line in [_.split('-') for _ in open(0).read().strip().split(',')]:
    L,R=[int(_)for _ in line]
    for n in range(L,R+1):
        s=str(n)
        l=len(s)
        if l%2==0 and s[:l//2]==s[l//2:]:
            res1+=n
    def p2b(): # definition of the repeated substr
        res=0
        for n in range(L,R+1):
            s=str(n)
            l=len(s)
            for sublen in range(1,l//2+1):
                if l % sublen != 0:
                    continue
                if s == s[:sublen]*(l//sublen):
                    res += n
                    break
        return res
    def p2a():
        res=0
        for n in range(L,R+1):
            s=str(n)
            l=len(s)
            for bloc in range(2,l+1):
                if l % bloc !=0 :
                    continue
                sub = l // bloc
                ok = True
                for i in range(0,l-sub+1,sub):
                    if s[:sub] != s[i:i+sub]:
                        ok = False
                if ok:
                    res += n
                    break
        return res
    res2 += p2b()
print(res1,res2)
assert res1 in (1227775554,55916882972)
assert res2 in (4174379265,76169125915)
