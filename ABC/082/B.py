s = input()
t = input()

if sorted(s) < sorted(t, reverse=True):
    print("Yes")
else:
    print("No")
