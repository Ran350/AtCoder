N = int(input())

result = 1
mod = 10**9 + 7

for i in range(2, N+1):
    result = (result*i) % mod

print(result)
