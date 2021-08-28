n = int(input())
inputs = list(map(int, input().split()))


def is_all_odd(l: list) -> bool:
    for e in l:
        if (e % 2 == 1):
            return False
    return True


count = 0

while True:
    if not is_all_odd(inputs):
        break

    count += 1
    inputs = [i/2 for i in inputs]

print(count)
