from itertools import permutations

S, K = input().split()
K = int(K)

words = {"".join(p) for p in permutations(S)}

words = sorted(list(words))

print(words[K-1])
