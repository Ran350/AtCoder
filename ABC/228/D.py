Q = int(input())
TX = [[int(x) for x in input().split()] for i in range(Q)]

N = 2 ** 20
A = [-1] * N

nx = list(range(1, N)) + [0]


def update(h, x):
    if A[h] == -1:
        A[h] = x
        return h

    nx[h] = update(nx[h], x)

    return nx[h]


for (t, x) in TX:
    if t == 1:
        update(x % N, x)
    if t == 2:
        print(A[x % N])
