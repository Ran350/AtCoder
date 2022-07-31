N,K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
XY = [tuple(int(x) for x in input().split()) for _ in range(N)]

print(XY)

for xy in XY:
    for a in A:
        