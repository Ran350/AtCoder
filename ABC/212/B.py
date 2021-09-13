X = [int(x) for x in input()]

if len(set(X)) == 1:
    print("Weak")

elif all([(X[i]+1) % 10 == X[i+1] for i in range(len(X)-1)]):
    print("Weak")

else:
    print("Strong")
