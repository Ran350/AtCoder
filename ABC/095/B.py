N, X = [int(_) for _ in input().split()]
M = [int(input()) for _ in range(N)]

print(len(M) + (X - sum(M)) // min(M))
