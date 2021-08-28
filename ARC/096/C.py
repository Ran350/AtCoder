A, B, AB, X, Y = [int(_) for _ in input().split()]

if X > Y:
    mix = 2*AB*Y + A*(X-Y)  # Y枚のABと残りはA
else:
    mix = 2*AB*X + B*(Y-X)  # X枚のABと残りはB

price = min(
    A*X + B*Y,       # ABなし
    2*AB*max(X, Y),  # ABのみ
    mix
)

print(price)
