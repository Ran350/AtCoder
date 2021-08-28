N = int(input())
plans = [[int(x) for x in input().split()] for _ in range(N)]


old_t, old_x, old_y = 0, 0, 0

for plan in plans:
    t, x, y = plan

    distance = abs(x-old_x) + abs(y-old_y)

    if distance > t-old_t:
        print("No")
        exit()

    if (t-old_t - distance) % 2 == 1:
        print("No")
        exit()

    old_t, old_x, old_y = t, x, y

print("Yes")
