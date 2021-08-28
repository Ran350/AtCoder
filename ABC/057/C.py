from math import sqrt

N = int(input())

ans = len(str(N)) + 1

for i in range(1, int(sqrt(N)) + 1):
    if N % i == 0:
        length = max(len(str(i)), len(str(N//i)))
        ans = min(ans, length)

print(ans)
