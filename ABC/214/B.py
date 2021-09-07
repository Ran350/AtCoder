S, T = [int(_) for _ in input().split()]

count = 0

for a in range(S + 1):
    for b in range(S-a + 1):
        for c in range(S-a-b + 1):
            if a * b * c <= T:
                count += 1

print(count)
