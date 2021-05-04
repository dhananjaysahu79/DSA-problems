#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# Input: nums = [1,2,3]
# Output: [1,3,2]

# ~ O(n) solution.

arr = list(map(int,input().split()))
l = -1
n = len(arr)

for i in range(n-1,0,-1):      # Finding the breakpoint. O(n)
    if arr[i] > arr[i-1]:
        l = i+1
        break

if l != -1:
    for i in range(n-1,l,-1):  # Searching the element greater than the element at breakpoint index. O(n)
        if arr[i] > arr[l]:
            arr[i],arr[l] = arr[l],arr[i]

m = n - 1
while m >= l:                  # reversing the array from breakpoint index +1 to the last. O(n)
    arr[m],arr[l] = arr[l],arr[m]
    m -= 1

print(*arr)

