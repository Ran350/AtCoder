N = int(input())
A = [int(x) for x in input().split()]
X = int(input())

A_sum = sum(A)
k = (X // A_sum) * len(A)
remainder = X % A_sum

i = 0
while remainder >= 0:
    remainder -= A[i]
    k += 1
    i += 1

print(k)
