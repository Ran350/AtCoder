from itertools import combinations

N = int(input())
L = [int(_) for _ in input().split()]

count = 0

for pair in combinations(L, 3):
    if len(pair) != len(set(pair)):
        continue

    if max(pair) < sum(pair) - max(pair):
        count += 1

print(count)
