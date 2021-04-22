# take an input n and print the pattern like that.
# Input => 2
# 2 2 2
# 2 1 2
# 2 2 2

# Input => 5
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5

# python 3 solution

n = int(input())
for i in range(-n+1,n):
    for j in range(-n+1,n): print(max(abs(i),abs(j)) + 1,end = ' ')
    print("\n", end = "")