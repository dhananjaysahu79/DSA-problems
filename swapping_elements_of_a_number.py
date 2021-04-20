# input a number and swap all the characters to
# 0 => 9, 1 => 8 , 2 => 7........9 => 0
# if the number is greater than 1000000 then print "Wrong Input"
# Python 3 solution
n = input()
print("Wrong Input" if int(n) > 1000000 else ''.join([str(9-int(i)) for i in n]),sep='')
