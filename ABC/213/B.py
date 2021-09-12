N = int(input())
A = [int(_) for _ in input().split()]

BB_score = sorted(A)[-2]

print(A.index(BB_score) + 1)
