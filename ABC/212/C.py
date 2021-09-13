N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort()

ans = float('inf')

a_i = 0
b_i = 0

while a_i < N and b_i < M:
    ans = min(ans, abs(A[a_i] - B[b_i]))

    if A[a_i] > B[b_i]:
        b_i += 1
    else:
        a_i += 1

print(ans)
