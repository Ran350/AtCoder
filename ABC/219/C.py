X = input()
N = int(input())
S = [list(input()) for _ in range(N)]

# 各文字を新辞書の番号に変換
new_dict = {x: i for i, x in enumerate(X)}
S = [[new_dict[c] for c in s] for s in S]

S.sort()

# 各新辞書番号を文字に変換
new_dict = {i: x for i, x in enumerate(X)}
S = [[new_dict[c] for c in s] for s in S]


for s in S:
    print("".join(s))
