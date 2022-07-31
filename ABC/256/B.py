N = int(input())
A = [int(x) for x in input().split()]

sums = A[-1] + [0]*(len(A)-1)

for i in range(1, len(A)):
    sums[-i-1] += sums[-i] + A[-i-1]

ans = len(list(filter(lambda x: x > 3, sums)))

print(ans)