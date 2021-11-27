N, K = [int(x) for x in input().split()]
P = [[int(x) for x in input().split()] for i in range(N)]

points = [[sum(point), i] for i, point in enumerate(P)]
points.sort(reverse=True)

ans = ["No"]*N

border = points[K-1][0]

for (point, i) in points:
    if point + 300 >= border:
        ans[i] = "Yes"

for a in ans:
    print(a)
