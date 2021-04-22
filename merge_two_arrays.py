# given two sorted arrays,merge them in O(1) space complexity.
# pYthon 3 solution

# In this approach we will take all the smaller elements and fill it in first array.

# we will take a variable m that points to the last element of first array,
# because that would be the highest number in first array, right?
# traversing through the element of both the array, if at any point we find the element that is greater in
# first arary than in second array we will swap the element at index m of first array with the smaller number
# just found in second array. we will do these steps until whole second array is traversed
# or a crosses the m.

# after that it doesn't guarantee that both the array will be sorted. so we need to sort both the array


arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

a = 0; b = 0; m = len(arr1) - 1

while a <= m and b < len(arr2):
    if arr1[a] > arr2[b]:
        arr1[m],arr2[b] = arr2[b],arr1[m]
        b += 1
        m -= 1
    else: a += 1
arr1.sort()
arr2.sort()
print(*arr1,*arr2)