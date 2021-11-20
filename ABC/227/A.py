N, K, A = [int(x) for x in input().split()]

ans = A + (K % N) - 1

if N == 1:
    print(1)
elif ans > N:
    print(ans % N)
else:
    print(ans)
