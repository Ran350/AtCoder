N = int(input())
P = [int(_) for _ in input().split()]

Q = [0]*N
for i, p in enumerate(P):
    Q[p-1] = i+1

print(*Q)
