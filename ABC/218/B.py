from string import ascii_lowercase

P = [int(_) for _ in input().split()]

ans = [ascii_lowercase[p-1] for p in P]

print("".join(ans))
