from itertools import chain

N, M = [int(_) for _ in input().split()]
paths = [[int(_) for _ in input().split()] for i in range(M)]

flattens = list(chain.from_iterable(paths))

for i in range(1, N+1):
    print(flattens.count(i))
