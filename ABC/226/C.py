N = int(input())

T = []
A = []
for _ in range(N):
    tka = [int(_) for _ in input().split()]
    T.append(tka[0])
    A.append(tka[2:])

is_acquires = [False]*(N-1) + [True]

for i in reversed(range(N)):
    if not is_acquires[i]:
        continue
    for c in A[i]:
        is_acquires[c-1] = True

time = 0
for i in range(N):
    if is_acquires[i]:
        time += T[i]

print(time)
