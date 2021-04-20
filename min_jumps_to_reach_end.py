# Minimum jumps to reach the end of an array.If there is no possible way to do it output -1
# 2 1 5 6 3 2
# output => 2
# explanation => (2 => 5 => end) by default position will be on the first element
# with that value of first element we can either jump on index 1 or 2.We will jump to 2 as the
# value at index 2 is greater. after reaching index 2,value there is 5, now we have 5 options
# we can jump to index 3,4,5 or end. we will jump to the end.
# python 3 O(n) solution

#Approach => We will take a function calJump() that will calculate the number of jumps required to
# reach the end.
# we will take three variables
# 1. steps => to store number of steps where we could find max elements
# 2. maxReach => maximum position from an index we can jump
# 3. number of jumps taken.

def calJump(arr,n):
    if n == 1:
        return 0
    if arr[0] == 0: #if first element has no option to jump, then we cant reach end.
        return -1
    steps = arr[0]
    maxReach = arr[0]
    jumps = 1
    for i in range(1,n):
        if i == n-1: return jumps # as we reach the end element we will return the jump
        maxReach = max(maxReach,arr[i]+i) #updating the variable with the maximum reach possible
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= maxReach: return -1 # if we didnt get number greater than zero in the steps to jump
            steps = maxReach - i #subtracting i from max reach bcoz we have already traversed till i
arr = list(map(int,input().split()))
print(calJump(arr,len(arr)))