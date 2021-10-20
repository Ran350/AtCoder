S = input()

shifteds = [S[i:] + S[:i] for i in range(len(S))]

print(min(shifteds))
print(max(shifteds))
