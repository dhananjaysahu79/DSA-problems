# Input : s[] = {1, 3, 0, 5, 8, 5}, f[] = {2, 4, 6, 7, 9, 9}
# Output : 1 2 4 5

# O(n^2) and O(n) space
s = list(map(int,input().split()))
f = list(map(int,input().split()))
arr = []
for i in range(len(s)):
    arr.append([f[i],s[i],i+1])
arr.sort()
ans = []
prev_end_time = arr[0][0]
ans.append(arr[0][2])
for i in arr[1::]:
    if i[1] > prev_end_time:
        ans.append(i[2])
        prev_end_time = i[0]
print(ans)