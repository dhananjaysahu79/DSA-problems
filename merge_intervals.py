# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
stack = []
arr.sort()
stack.append(arr[0])
for i in arr[1:]:
    if i[0] <= stack[-1][1]:
        stack[-1][1] = max(i[1],stack[-1][1])
    else:
        stack.append(i)
print(stack)