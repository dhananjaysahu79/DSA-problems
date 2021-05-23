arr = list(map(int,input().split()))
curr_max = curr_min = ans = arr[0]
for i in arr[1:]:
    curr_max, curr_min = max(i, i * curr_max, i * curr_min), min(i, i * curr_min, i * curr_max)
    ans = max(curr_max, ans)
print(ans)