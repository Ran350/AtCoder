S = input()
K = int(input())

# . の数の累積和
T = [0]
for i in range(len(S)):
    if S[i] == ".":
        T.append(T[-1] + 1)
    else:
        T.append(T[-1])

ans = 0
right = 0

# 尺取り法
for left in range(len(S)):
    while right < len(S) and T[right+1] - T[left] <= K:  # 範囲内を全て X に変更可能
        right += 1

    ans = max(ans, right - left)

print(ans)
