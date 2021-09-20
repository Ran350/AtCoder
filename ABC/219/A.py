X = int(input())

scores = [40, 70, 90]

for score in scores:
    if 0 <= X < score:
        print(score - X)
        exit()

print("expert")
