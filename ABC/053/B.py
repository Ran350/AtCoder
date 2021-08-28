s = input()

start = s.index("A")
end = len(s) - s[::-1].index("Z")
print(end - start)
