N = int(input())

for i in range(N//7 + 1):
    if (N - 7*i) % 4 == 0:
        print("Yes")
        exit()
print("No")
