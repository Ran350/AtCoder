N = int(input())
A = [int(input()) for _ in range(N)]

count = 0
i = 0

for _ in range(N):
    count += 1

    if A[i] == 2:
        print(count)
        exit()

    i = A[i] - 1

print(-1)
