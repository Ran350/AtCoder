a, b, x = map(int, input().split())


def f(n, mod):
    if n < 0:
        return 0
    return n // mod + 1


print(f(b, x) - f(a-1, x))
