#Longest consecutive subaray
#Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
# Output: 4
# Explanation:
# The subsequence 1, 3, 4, 2 is the longest
# subsequence of consecutive elements

# approach: We will find the lowest number of each posibble subarray, and from there we will
# calculate the count the consecutives.
# How its O(n) time complexity ?
# since we only execute the loop if we get the lowest number of possible subarray, and rest we leave,
# and remaining in searching those consecutives.

arr = list(map(int,input().split()))
mx = 0
s = set(arr)
for i in s:
    if i-1 not in s:
        c = 1; curr_num = i + 1
        while curr_num in s:
            c+=1
            curr_num+=1
        mx = max(c,mx)
print(mx)