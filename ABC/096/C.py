H, W = map(int, input().split())
S = [input() for _ in range(H)]

flag = True

for y in range(H):
    for x in range(W):
        # #マスだけに着目
        if S[y][x] != "#":
            continue

        dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in dxy:
            # 4近傍が範囲外のとき
            if (x+dx < 0 or W-1 < x+dx) or (y+dy < 0 or H-1 < y+dy):
                continue

            if S[y+dy][x+dx] == "#":
                break

        else:
            flag = False

print("Yes" if flag else "No")
