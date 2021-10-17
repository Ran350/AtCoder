n = int(input())

ans = n

for i in range(1, int(n**0.5) + 1):
    ans = min(
        ans,
        abs(n//i - i) + n % i)  # 縦横差 + 余り枚数

print(ans)
