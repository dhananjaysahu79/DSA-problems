#Rearrange array in alternating negative and positive numbers
# Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}

# Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

# O(n) solution with O(n) space
# a - used to track negative numbers
# b - used to track positive numbers.
# f - used to store the current requirement whether we need positive and negative at certain index.
# ie. -1 means current requirement is negative number and 1 means positive numbers.
arr = list(map(int,input().split()))
if len(arr) < 2: print (*arr)
else:
    a = 0 ; b = 0 ; f = -1
    ans = []
    while a < len(arr) and b < len(arr):
        if f == -1:
            if arr[a] < 0:
                ans.append(arr[a])
                f = 1
            a+=1
        else:
            if arr[b] >= 0:
                ans.append(arr[b])
                f = -1
            b+=1
    while a < len(arr):
        if arr[a] < 0:ans.append(arr[a])
        a+=1
    while b < len(arr):
        if arr[b] >= 0:ans.append(arr[b])
        b+=1
    print(*ans)

# if the order of the elements doesn't matters
# it could be solved in O(n) time and O(1) space
# i : used for index to put the elements a/c to the requirement.
# a : pointer to find the negative elements.
# b : pointer to find the positive elements.

arr = list(map(int,input().split()))
a = b = i = 0
while a < len(arr) and b < len(arr):
    if i % 2:
        if arr[b] >= 0:
            arr[i],arr[b] = arr[b],arr[i]
            i+=1
        b+=1
    else:
        if arr[a] < 0:
            arr[i],arr[a] = arr[a],arr[i]
            i+=1
        a+=1
print(*arr)
