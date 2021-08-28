N = int(input())
T, A = [int(_) for _ in input().split()]
H = [int(_) for _ in input().split()]

diffs = [abs(T - h*0.006 - A) for h in H]

print(diffs.index(min(diffs)) + 1)
