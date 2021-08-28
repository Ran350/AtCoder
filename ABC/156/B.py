N, K = [int(_) for _ in input().split()]


def base_10_to_n(X: int, n: int):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n) + str(X % n)
    return str(X % n)


print(len((base_10_to_n(N, K))))
