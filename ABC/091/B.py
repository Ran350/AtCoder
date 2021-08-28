N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

price = 0

for word in (set(S) | set(T)):
    price = max(price, S.count(word) - T.count(word))

print(price)
