A, B, C, D = [int(_) for _ in list(input())]

op_s = (-1, 1)

for b in op_s:
    for c in op_s:
        for d in op_s:
            if A + b*B + c*C + d*D == 7:
                def op(arg):
                    return "+" if arg == 1 else "-"

                print(A, op(b), B, op(c), C, op(d), D, "=7", sep='')
                exit()
