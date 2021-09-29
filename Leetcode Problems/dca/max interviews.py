n = int(input())
start = []
for _ in range(n): start.append(int(input()))
end = []
for _ in range(n): end.append(int(input()))

c = 1; prev = end[0]
for i in range(1,n):
    if start[i] > prev:
        c += 1
        prev = end[i]
print(c)