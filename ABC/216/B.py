N = int(input())
ST = [input() for _ in range(N)]

if len(ST) == len(set(ST)):
    print("No")
else:
    print("Yes")
