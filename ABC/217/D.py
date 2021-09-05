from bisect import insort, bisect
from array import array

L, Q = [int(_) for _ in input().split()]
CX = [[int(_) for _ in input().split()] for _ in range(Q)]

points = array('I', [0, L])

for c, x in CX:
    if c == 1:
        insort(points, x)

    if c == 2:
        i = bisect(points, x)
        print(points[i] - points[i-1])
