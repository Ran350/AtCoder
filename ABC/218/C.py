from collections import deque


N = int(input())
S = deque([deque(list(input())) for _ in range(N)])
T = deque([deque(list(input())) for _ in range(N)])


def remove_padding(table: deque):
    # . のみの端の行 / 端の列をすべて削除

    while table[0].count("#") == 0:
        table.popleft()

    while table[-1].count("#") == 0:
        table.pop()

    while all([row[0] == "." for row in table]):
        for i in range(len(table)):
            table[i].popleft()

    while all([row[-1] == "." for row in table]):
        for i in range(len(table)):
            table[i].pop()


remove_padding(S)
remove_padding(T)


# 2次元dequeを 2次元listに変換
S = [list(s) for s in S]
T = [list(t) for t in T]


for _ in range(4):
    # 90° 回転
    S = [list(e) for e in zip(*S[::-1])]

    # S,Tが同じ要素数か
    if len(S) != len(T) or len(S[0]) != len(T[0]):
        continue

    # 2つの2次元配列が同じ値か
    if all([s == t for s, t in zip(S, T)]):
        print("Yes")
        exit()

print("No")
