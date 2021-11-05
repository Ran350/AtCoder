H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for i in range(H)]

for i2 in range(1, H):
    for i1 in range(i2):
        for j2 in range(1, W):
            for j1 in range(j2):
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    print("No")
                    exit()

print("Yes")
