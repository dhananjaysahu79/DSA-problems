# Two sum
# print any two index whose sum is equal to a given number.
#Input: [2,7,11,15] , target = 9
#Output: [0,1]

#1 The naive approach would be to traverse all possible pairs and find their sun, but that would be O(n).
#2 Another approach would be sorting the given array but storing its indexes to another 2-D array first,
#  then using two pointer (one pointing to the start and another end of array) we can find a pair. But
#  sorting would take O(nlogn)

#3 O(n) - Using hashmap or dictionary in python
# So the idea is to take a dictionary, and then traverse through the array from start, checking each number and store
# the requirement element in the dictionary that can achieve the sum. For example : if the element is 2 then we need 7 to
# make the target number. So we will store 7, and when we find 7 during traversing, we will simply return the index, that is
# stored in dictionary and the current index of the element for second number.

arr = list(map(int,input().split()))
target = int(input())
dic = {}
for i in range(len(arr)):
    if arr[i] in dic:
        print(dic[arr[i]],i)
        break
    dic[target - arr[i]] = i  # a+b = target, we just need to store the b(that is requirement so that it can make the sum possible)
                              # that is b = target - a
