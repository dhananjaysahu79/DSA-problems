def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        mergeSort(arr1)
        mergeSort(arr2)

        i = j = 0
        temp = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                temp.append(arr1[i])
                i+=1
            else:
                temp.append(arr2[j])
                j+=1
        while i < len(arr1):
            temp.append(arr1[i])
            i+=1
        while j < len(arr2):
            temp.append(arr2[j])
            j+=1
        for i in range(len(temp)): arr[i] = temp[i]

arr = list(map(int,input().split()))
mergeSort(arr)
print(*arr)