from heapq import heapify, heappop, heappush

N, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]

directed = [set() for i in range(N)]
directing = [set() for i in range(N)]
for a, b in AB:
    directed[b-1].add(a-1)
    directing[a-1].add(b-1)

empties = [i for i in range(len(directed)) if not directed[i]]
heapify(empties)

ans = []

while empties:
    from_point = heappop(empties)

    for to_point in directing[from_point]:
        directed[to_point].remove(from_point)

        if not directed[to_point]:
            heappush(empties, to_point)

    ans.append(from_point)

if len(ans) == N:
    print(" ".join([str(a+1) for a in ans]))
else:
    print(-1)
