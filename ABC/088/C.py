C = [[int(x) for x in input().split()] for _ in range(3)]


def check(field: list):
    diffs = [[row[0]-row[1], row[1]-row[2], row[2]-row[0]] for row in field]

    for i in range(3):
        if not diffs[0][i] == diffs[1][i] == diffs[2][i]:
            return False
    return True


if check(C) and check(list(zip(*C))):
    print("Yes")
else:
    print("No")
