A, B = [int(_) for _ in input().split()]

if 0 < A and 0 < B:
    print("Alloy")

elif B == 0:
    print("Gold")

elif A == 0:
    print("Silver")
