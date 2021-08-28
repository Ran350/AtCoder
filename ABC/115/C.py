from sys import maxsize

N, K = [int(_) for _ in input().split()]
H = [int(input()) for _ in range(N)]

H.sort()

ans = maxsize

for i in range(len(H) - K + 1):
    ans = min(ans, H[i+K-1] - H[i])

print(ans)
