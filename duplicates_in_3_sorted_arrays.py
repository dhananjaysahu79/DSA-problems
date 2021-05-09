# Input:
# ar1[] = {1, 5, 10, 20, 40, 80}
# ar2[] = {6, 7, 20, 80, 100}
# ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20, 80

#  O( m + n + o)

# So the approach is to take three pointers pointing to the three arrays, we will traverse to the end of the arrays
# when we find the smallest element among all the arrays for their current index we will increament that pointer by 1.
# when we find equals we will print that value.

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = list(map(int,input().split()))
i = j = k = 0
while i < len(arr1) and j < len(arr2) and k < len(arr3):
    a = i; b = j; c = k
    if arr1[i] == arr2[j] == arr3[k]:
        print(arr1[i],end=' ')
    if arr1[a] <= arr2[b] and arr1[a] <= arr3[c]: i+=1
    if arr2[b] <= arr1[a] and arr2[b] <= arr3[c]: j+=1
    if arr3[c] <= arr1[a] and arr3[c] <= arr2[b]: k+=1

