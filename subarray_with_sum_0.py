# input: 3 1 3 -4 8 7
# output: True


arr = list(map(int,input().split()))
ans = False
sumset = set()
sm = 0
for i in arr:
    sm += i
    if sm in sumset or sm == 0:
        ans = True
        break
    else: sumset.add(sm)
print(ans)