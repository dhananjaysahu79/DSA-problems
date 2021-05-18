# if you're using python this is the oneliner

import math
print(math.factorial(int(input())))

#if you don't know math.factorial exist. just do how you used to to it.
n = int(input())
f = 1
while n > 1:
    f = f * n
    n -= 1
print(f)

# a naive solution: how you used to multiply big numbers in your 5th grade.
num = input()
fac = '1'
while num != '1':
    curr_fact = '0'; c = 0
    for i in num[::-1]:
        carry = 0; f = ''
        for j in fac[::-1]:
            temp = int(i) * int(j) + carry
            carry = temp // 10
            f = f + str(temp % 10)
        if carry: f += str(carry)
        temp = f[::-1] + ('0' * c)
        curr_fact = str(int(curr_fact) + int(temp))
        c+=1
    fac = curr_fact
    num = str(int(num) - 1)
print(fac)

# Again a naive solution but with better time complexity(since n is small
# so we dont need to compute it as a string. Hence one nested loop is reduced)

n = int(input())
fac = '1'
while n > 1:
    carry = 0; curr_product = ''
    for i in fac[::-1]:
        temp = int(i) * n + carry
        carry = temp // 10
        curr_product = curr_product + str(temp % 10)
    u = str(carry)
    if carry: curr_product = curr_product + u[::-1]
    fac = curr_product[::-1]
    n -= 1
print(fac)