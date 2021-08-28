H, W = [int(i) for i in input().split()]
S = [list(input()) for _ in range(H)]


for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            continue

        count = 0

        dxy = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]

        for dx, dy in dxy:
            # 8近傍が範囲外なら
            if (x+dx < 0 or W-1 < x+dx) or (y+dy < 0 or H-1 < y+dy):
                continue

            if S[y+dy][x+dx] == "#":
                count += 1

        S[y][x] = str(count)


for row in S:
    print("".join(row))
