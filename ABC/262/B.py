from itertools import combinations

N, M = [int(x) for x in input().split()]
UV = tuple(input().split() for _ in range(M))

G = {str(i) : set() for i in range(1, N+1)}
for (u,v) in UV:
    G[u].add(v)
    G[v].add(u)

count = 0

for key in G:
    for (a, b) in combinations(G[key], 2):
        if b in G[a]:
            count += 1

print(count // 3)
