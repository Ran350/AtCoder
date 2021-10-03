S = list(input())
T = list(input())

hasSwapped = False

for i in range(len(S)-1):
    if S[i] == T[i]:
        continue

    if hasSwapped == True:
        print("No")
        exit()

    T[i], T[i+1] = T[i+1], T[i]
    hasSwapped = True

print("Yes")
