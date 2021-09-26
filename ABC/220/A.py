A, B, C = [int(x) for x in input().split()]

for i in range(A, B+1):
    if i % C == 0:
        print(i)
        exit()
print(-1)
