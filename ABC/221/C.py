N = list(input())

N.sort(reverse=True)

X = N[0::2]
Y = N[1::2]

for i in range(len(Y)):
    if X[i] != Y[i]:
        X[i], Y[i] = Y[i], X[i]
        break

print(int("".join(X)) * int("".join(Y)))
