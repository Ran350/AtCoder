from sys import maxsize

N = int(input())
S = [int(_) for _ in input().split()]
T = [int(_) for _ in input().split()]


ans = [maxsize] * N

for i in range(2 * N):
    pre_sunuke = ans[i % N] + S[i % N]
    takahashi = T[(i + 1) % N]

    ans[(i + 1) % N] = min(pre_sunuke, takahashi)


for a in ans:
    print(a)
