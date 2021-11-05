# we know that, sum of n numbers can be written as x * (x+1) // 2
# here, in this case sum is given and we have to find the x

# So we can write it as
# x*x + x - 2n = 0
# note: here n is given in the question.

# Now we can use the traditional technique to find the root of the above equation,
# d (discriminant) = sqrt(b*b - 4ac)
# So here in this case,
# a = 1
# b = 1
# c = -2n
# then we will use,
# x1 (root) = (-b + d) // 2
# and
# x2(root) = (-b - d) // 2
# we will ignore x2 because it will always give us the negative results.

# lastly we will return the integer value of the root.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        d = (1 + (4 * 1 * 2 * n)) ** 0.5

        x = int((-1 + d) // 2)

        return x