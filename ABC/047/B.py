W, H, N = [int(_) for _ in input().split()]
xya = [[int(_) for _ in input().split()] for _ in range(N)]

field = [[0] * W for _ in range(H)]

for xi, yi, ai in xya:
    if ai == 1:
        for y in range(H):
            for x in range(xi):
                field[y][x] = 1

    if ai == 2:
        for y in range(H):
            for x in range(xi, W):
                field[y][x] = 1

    if ai == 3:
        for y in range(yi):
            for x in range(W):
                field[y][x] = 1

    if ai == 4:
        for y in range(yi, H):
            for x in range(W):
                field[y][x] = 1


print(sum([row.count(0) for row in field]))
