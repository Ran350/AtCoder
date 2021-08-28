from sys import maxsize

N = int(input())

ans = maxsize

for i in range(1, N):
    def digits_sum(integer):
        l = list(str(integer))
        return sum(int(v) for v in l)

    A = i
    B = N-i

    ans = min(ans, digits_sum(A) + digits_sum(B))

print(ans)
