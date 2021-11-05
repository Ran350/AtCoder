N = int(input())
AB = [{int(x) for x in input().split()} for i in range(N-1)]

root = set(range(1, N+1))

for ab in AB:
    root = root.intersection(ab)

if root:
    print("Yes")
else:
    print("No")
