N, M = [int(x) for x in input().split()]
A = [list(input()) for i in range(2*N)]

ranks = [[0, i] for i in range(len(A))]
# [[ 勝利数*(-1), プレイヤ番号 ],]
# *(-1) は後の昇順ソート用


def judge(hand1: str, hand2: str):
    # 引き分け
    if hand1 == hand2:
        return 0

    # hand1勝ち
    if (
        hand1 == "G" and hand2 == "C" or
        hand1 == "C" and hand2 == "P" or
        hand1 == "P" and hand2 == "G"
    ):
        return 1

    # hand1負け
    return -1


for j in range(M):
    for i in range(N):
        player1 = ranks[2*i]
        player1_id = player1[1]
        player1_hand = A[player1_id][j]

        player2 = ranks[2*i + 1]
        player2_id = player2[1]
        player2_hand = A[player2_id][j]

        result = judge(player1_hand, player2_hand)

        if result == 1:
            player1[0] -= 1
        if result == -1:
            player2[0] -= 1

        # 2重配列ごとソート
        ranks.sort()

for rank in ranks:
    print(rank[1] + 1)
