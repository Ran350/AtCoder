N = int(input())
LR = [[int(x) for x in input().split()] for _ in range(N)]

LR.sort()
ranges = [LR[0]]

for i in range(1,len(LR)):
    if LR[i][0] > ranges[-1][1]:
        ranges.append(LR[i])
        continue
    if LR[i][1] > ranges[-1][1]:
        ranges[-1][1] = LR[i][1]

for r in ranges:
    print(r[0], r[1])
