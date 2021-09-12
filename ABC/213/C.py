H, W, N = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]
A, B = list(zip(*AB))

A_dict = {a: i+1 for i, a in enumerate(sorted(set(A)))}
B_dict = {b: i+1 for i, b in enumerate(sorted(set(B)))}
# {A,Bの値 : 昇順で何番目か}

for i in range(N):
    print(A_dict[A[i]], B_dict[B[i]])
