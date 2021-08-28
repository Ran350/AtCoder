c500 = int(input())
c100 = int(input())
c50 = int(input())
sum = int(input())

count = 0

for i in range(c500+1):
    for j in range(c100+1):
        for k in range(c50+1):
            if(500*i + j*100 + k*50 == sum):
                count += 1

print(count)
