from scipy.special import comb

N = int(input())
A = [int(x) for x in input().split()]

same = 0 
diff = 0 

for i, a in enumerate(A):
    if a == i + 1:      # a_i = i && a_j = j
        same += 1
    elif A[a-1] == i+1: # a_i = j && a_j = i
        diff += 1

print(
    same * (same-1) // 2
    +
    diff // 2 
)