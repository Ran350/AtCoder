N = int(input())
A1 = [int(_) for _ in input().split()]
A2 = [int(_) for _ in input().split()]

candy = 0

for i in range(N):
    route = A1[:i+1] + A2[i:]
    candy = max(candy, sum(route))

print(candy)
