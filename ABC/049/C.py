S = input()
T = ""
words = ["dream", "dreamer", "erase", "eraser"]

while not S == "":
    old_S = S

    for word in words:
        if S[-len(word):] == word:  # 後ろn文字を比較
            S = S[:-len(word)]  # 後ろn文字を削除
            break

    if old_S == S:
        print("NO")
        exit()

print("YES")
