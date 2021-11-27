N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

known = set()
known.add(X)

next_friend = A[X-1]

while True:
    known.add(next_friend)
    next_friend = A[next_friend-1]

    if next_friend in known:
        break

print(len(known))
