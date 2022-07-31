MOD = 998244353

N = int(input())
A = [int(x) for x in input().split()]

ans = 0

for i in range(1, N+1): # N個 の中から i個選ぶ
    # dp_{j,k,l}：先頭j項目 の中から k個選んで 総和をiで割ったあまりがl
    dp = [[[0] * i for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for j in range(1, N+1):
        for k in range(j+1):
            for l in range(i):
                dp[j][k][l] += dp[j-1][k][l]
                if k != 0:
                    dp[j][k][l] += dp[j-1][k-1][(l + i - A[j-1]) % i]
                dp[j][k][l] %= MOD

    # dp_{N,i,0} の総和
    ans += dp[-1][i][0]
    ans %= MOD

print(ans)