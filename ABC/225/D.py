N, Q = [int(x) for x in input().split()]
queries = [[int(x) for x in input().split()] for i in range(Q)]

trains = {i: {"front": None, "back": None} for i in range(1, N+1)}


def query1(x, y):
    trains[x]["back"] = y
    trains[y]["front"] = x


def query2(x, y):
    trains[x]["back"] = None
    trains[y]["front"] = None


def query3(x):
    # 先頭電車の探索
    head = x
    while trains[head]["front"] != None:
        head = trains[head]["front"]

    # 連結電車の探索
    ans = []
    i = head
    while i != None:
        ans.append(i)
        i = trains[i]["back"]

    print(len(ans), *ans)


for query in queries:
    if query[0] == 1:
        query1(query[1], query[2])

    if query[0] == 2:
        query2(query[1], query[2])

    if query[0] == 3:
        query3(query[1])
