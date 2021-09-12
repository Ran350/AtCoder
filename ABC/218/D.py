from itertools import combinations


N = int(input())
XY = {tuple(input().split()) for _ in range(N)}

count = 0

# 長方形の対角となる頂点の組を全探索
for (x1, y1), (x2, y2) in combinations(XY, 2):
    if x1 == x2 or y1 == y2:
        continue

    if (x1, y2) in XY and (x2, y1) in XY:
        count += 1

print(count // 2)
