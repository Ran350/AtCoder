A, B = input().split()

for i in range(1, min(len(A), len(B))+1):
    if int(A[-i]) + int(B[-i]) > 9:
        print("Hard")
        exit()

print("Easy")
