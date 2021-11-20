N = int(input())
S = [int(x) for x in input().split()]


def area(a, b):
    return 3*a + 3*b + 4*a*b


def is_hit(s):
    a = 1

    while area(a, 0) <= s:
        b = 1

        while area(a, b) <= s:
            if area(a, b) == s:
                return True
            b += 1

        a += 1

    return False


count = 0

for s in S:
    if not is_hit(s):
        count += 1

print(count)
