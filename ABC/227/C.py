N = int(input())

count = 0

for a in range(1, int((N+1)**(1/3))+1):
    for b in range(a,  int((N//a)**(1/2))+1):
        count += N // (a*b) - b + 1

print(count)
