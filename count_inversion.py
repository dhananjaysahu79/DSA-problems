# Given an array of integers. Find the Inversion Count in the array.

# Inversion Count: For an array, inversion count indicates how far (or close) the array is from
# being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in
# the reverse order then the inversion count is the maximum.
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
# Input: N = 5, arr[] = {2, 4, 1, 3, 5}
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5
# has three inversions (2, 1), (4, 1), (4, 3).

# Naive approch or brute force approach to solve this.
# Solution 1, O(n*n) approach
arr = list(map(int,input().split()))
count = 0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]: c+=1
print(count)


# Merge sort approach O(nlogn)

def cntInv(arr):
    count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        count += cntInv(arr1)
        count += cntInv(arr2)

        i = j = 0
        temp = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                temp.append(arr1[i])
                i+=1
            else:
                temp.append(arr2[j])
                count += len(arr1) - i
                j+=1
        while i < len(arr1):
            temp.append(arr1[i])
            i+=1
        while j < len(arr2):
            temp.append(arr2[j])
            j+=1
        for i in range(len(temp)): arr[i] = temp[i]
    return count

arr = list(map(int,input().split()))
print(cntInv(arr))