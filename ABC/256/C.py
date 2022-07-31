l = [int(x) for x in input().split()]
H, W = l[:3], l[3:]

count = 0

for ul in range(1, 29):
    for uc in range(1, 29):
        for cl in range(1, 29):
            for cc in range(1, 29):
                ur = H[0] - ul - uc
                cr = H[1] - cl - cc
                ll = W[0] - ul - cl
                lc = W[1] - uc - cc
                lr = H[2] - ll - lc
                
                if (ur > 0 and 
                    cr > 0 and 
                    ll > 0 and 
                    lc > 0 and
                    lr > 0 and
                    ur+cr+lr == W[2]):
                    count += 1

print(count)