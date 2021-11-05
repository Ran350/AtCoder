N, M = [int(x) for x in input().split()]
B = [[int(x) for x in input().split()] for i in range(N)]

s = B[0][0]

if (s-1) % 7 + M > 7:
    print("No")
    exit()

for i in range(N):
    for j in range(M):
        if B[i][j] != s + 7*i + j:
            print("No")
            exit()

print("Yes")
