S = {input() for _ in range(3)}

contests = {"ABC", "ARC", "AGC", "AHC"}
ans = contests - S

print(list(ans)[0])
