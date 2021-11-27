S, T, X = [int(x) for x in input().split()]

if(S < T):
    if (S <= X < T):
        print("Yes")
    else:
        print("No")
else:
    if (T <= X < S):
        print("No")
    else:
        print("Yes")
