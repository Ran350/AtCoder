from math import sqrt
from itertools import combinations


N, D = [int(_) for _ in input().split()]
X = [[int(_) for _ in input().split()] for i in range(N)]

count = 0

for pair in combinations(X, 2):
    l = [(pair[0][i] - pair[1][i]) ** 2 for i in range(D)]
    distance = sqrt(sum(l))

    if distance.is_integer():
        count += 1

print(count)
