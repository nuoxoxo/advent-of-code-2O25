lines = open(0).read().split('\n\n')[-1].splitlines()
res = 0
import re
for l in lines:
    x,y,*nums = list(map(int,re.findall(r'\d+',l)))
    if x//3 * y//3 >= sum(nums):
        res += 1
print(res)
