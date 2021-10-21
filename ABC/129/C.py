N, M = [int(x) for x in input().split()]
A = {int(input()) for _ in range(M)}
MOD = 1_000_000_007

dp = [0]*(N+1)  # i段目までの上り方 (x通り)
dp[0] = 1

for i in range(1, N+1):
    if i in A:
        continue

    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[-1])
