N, W = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for i in range(N)]

AB.sort(reverse=True)

delicious = 0

for (a, b) in AB:
    if W > b:
        W -= b
        delicious += a * b
    else:
        delicious += a * W
        break

print(delicious)
