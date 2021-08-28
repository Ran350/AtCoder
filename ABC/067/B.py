N, K = [int(_) for _ in input().split()]
L = [int(_) for _ in input().split()]

L.sort()
print(sum(L[-K:]))
