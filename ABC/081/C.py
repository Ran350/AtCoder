from collections import Counter

N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

buckets = list(Counter(A).values())

buckets.sort(reverse=True)

print(sum(buckets[K:]))
