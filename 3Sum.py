# Problem : Find all triplets whose sum is equal to 0, all triplets must be unique.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# A naive approach would be taking three loops and then check each and every triplets.
# But that would be O(n^3)

# An effient approach would be using two loops and two pointers appraoch, but we nees to
# sort the array for that.

# Let's look into it how we can do it.

arr = list(map(int,input().split()))
ans = []
arr.sort()
n = len(arr)
# Prerequisites are ready to hold stuffs.
# Now we will iterate through 0 to n-3 index taking an element from it as constant.
for i in range(0,n-2):
    a = i+1; b = n-1
    # Took two pointer one points to the start of the sorted array and another to the end.
    # skipping the duplicates constants.
    if i != 0 and arr[i] == arr[i-1]: continue
    # Now we will take another loop
    while a < b:
        if arr[i] + arr[a] + arr[b] == 0:
            ans.append([arr[i],arr[a],arr[b]])
            # We will simply append the triplets.
            # Now we have to handle the duplicates triplets. Since the array is sorted if two elements
            # are unique we just need to look into right and left of paricular index.
            while a < b and arr[a] == arr[a+1]: a+=1
            while a < b and arr[b] == arr[b-1]: b-=1
            # handled the duplicates sucessfully. Now we will increment and decrement the pointers
            # respectively to move to the next index.
            a+=1
            b-=1
        elif arr[i] + arr[a] + arr[b] > 0: b-=1 #if greater than 0, then it must be the greater value who is icreasing the sum.
        else: a+=1 # if lesser thamn 0 then it must be the lower value who is decreasing the sum, so take another one.
print(ans)