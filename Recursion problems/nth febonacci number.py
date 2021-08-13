# Febonacci numbers series: 0 1 1 2 3 5 8 13....
# 1st febonnaci number = 0
# 2nd febonacci number = 1
# nth febonacci number = febonaci of n - 1 + febonacci of n - 2
# Here we will do the same using recursion.


def nFebonacci(n):
    if n == 1: return 0
    if n == 2: return 1
    return nFebonacci(n-1) + nFebonacci(n - 2)
print(nFebonacci(int(input())))
