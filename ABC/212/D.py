import heapq

Q = int(input())

balls = []
heapq.heapify(balls)

augend = 0

for _ in range(Q):
    query = [int(x) for x in input().split()]

    if query[0] == 1:
        heapq.heappush(balls, query[1] - augend)

    elif query[0] == 2:
        # 配列全体への加算は遅い
        augend += query[1]

    elif query[0] == 3:
        print(heapq.heappop(balls) + augend)
