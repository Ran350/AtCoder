N = int(input())
W = [int(x) for x in input().split()]

S1 = S2 = 0
i = 0
j = len(W)-1

for _ in range(len(W)):
    if S1 < S2:
        S1 += W[i]
        i += 1
    else:
        S2 += W[j]
        j -= 1

print(abs(S1 - S2))
