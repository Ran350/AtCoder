N = int(input())
XY = [[int(x) for x in input().split()] for i in range(N)]

count = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            dy_ij = XY[j][1] - XY[i][1]
            dx_ij = XY[j][0] - XY[i][0]
            dy_jk = XY[k][1] - XY[j][1]
            dx_jk = XY[k][0] - XY[j][0]

            if dy_ij * dx_jk == dy_jk * dx_ij:
                # 2直線の傾きが等しく 一直線に並ぶ時
                # ZeroDivisionを避けるため dy/dxを積の形に
                continue

            count += 1

print(count)
