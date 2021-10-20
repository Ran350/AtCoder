N = int(input())
AB = [[int(x) for x in input().split()] for i in range(N)]

time = 0
for Ai, Bi in AB:
    time += Ai/Bi
time /= 2

ans = 0

for Ai, Bi in AB:
    ans += min(Ai, time * Bi)
    time -= min(Ai/Bi, time)

print(ans)
