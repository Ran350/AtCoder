n, a, b = map(int, input().split())

result = 0

for i in range(1, n+1):
    i_sum = sum([int(x) for x in str(i)])

    if a <= i_sum <= b:
        result += i

print(result)
