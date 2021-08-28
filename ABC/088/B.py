n = int(input())
a = list(map(int, input().split()))

player_sums = [0, 0]

a.sort(reverse=True)

for i in range(len(a)):
    player_sums[i % 2] += a[i]

print(player_sums[0]-player_sums[1])
