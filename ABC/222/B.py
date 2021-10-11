N, P = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

print(len([a for a in A if a < P]))
