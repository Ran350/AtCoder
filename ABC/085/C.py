N, Y = [int(i) for i in input().split()]

for i in range(N+1):
    for j in range(0, N-i+1):
        k = N - i - j
        if 10000*i + 5000*j + 1000*k == Y:
            print(f"{i} {j} {k}")
            exit()

print("-1 -1 -1")
