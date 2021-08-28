A, B, C = map(int, input().split())

old_remainders = []
i = 0

while True:
    i += 1
    remainder = A*i % B

    if remainder == C:
        print("YES")
        break

    if remainder in old_remainders:
        print("NO")
        break

    old_remainders.append(remainder)
