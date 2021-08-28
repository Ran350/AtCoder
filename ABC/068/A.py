N = int(input())

bins = [2**i for i in range(7)]

answer = 0

for bin in bins:
    if N < bin:
        break
    answer = bin

print(answer)
