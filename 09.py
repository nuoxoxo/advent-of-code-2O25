A = [tuple(map(int,_.split(','))) for _ in open(0).read().splitlines()]
N = len(A)
pairs = []
for i in range(N-1):
    for j in range(i+1,N):
        pairs.append(((A[i]),(A[j])))
areas = []
for p in pairs:
    ((a,b),(c,d)) = p
    areas.append((1+abs(a-c))*(1+abs(b-d)))
print('p1/',max(areas))

from shapely.geometry import Point,Polygon,box
import matplotlib.pyplot as plt

pts = [Point(x,y) for x,y in A]
plg = Polygon( pts )
#print('area/', plg.area, 'bounds/',plg.bounds)
x,y = plg.exterior.xy
plt.plot(x,y)
#plt.show()

p2 = 0
bestshape = None

# reuse the pair-set of all the points
# get all rects, check if the rect lies within polygon
# collect its area if ok

for ((a,b),(c,d)) in pairs:
    rect = box(min(a,c),min(b,d),max(a,c),max(b,d))
    if rect.within(plg):
        res = (1+abs(a-c))*(1+abs(b-d))
        if p2 < res:#rect.area:
            p2 = res#rect.area
            bestshape = rect

print('p2/',p2)
#rect = Polygon( bestshape )
x2,y2 = Polygon( bestshape ).exterior.xy
plt.plot(x2,y2)
plt.show()
