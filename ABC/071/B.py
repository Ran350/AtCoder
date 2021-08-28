from string import ascii_lowercase

S = input()

not_founds = set(ascii_lowercase) - set(S)

if not_founds:
    print(min(list(not_founds)))
else:
    print(None)
