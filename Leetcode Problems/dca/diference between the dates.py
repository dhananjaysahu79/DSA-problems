dic = [
    ['January', 31],
    ['February', 29],
    ['March', 31],
    ['April',30],
    ['May',  31],
    ['June', 30],
    ['July', 31],
    ['August', 31],
    ['September', 30],
    ['October', 31 ],
    ['November', 30],
    ['December', 31]
]
dd,mm = int(input()), input()
left = 183
curr_index = 0
for i in range(len(dic)):
    if dic[i][0] == mm:
        curr_index = i
        break
left -= (dic[curr_index][1] - dd)
curr_index = (curr_index + 1) % 12
while left > 0:
    if left > dic[curr_index][1]:
        left -= dic[curr_index][1]
        curr_index = (curr_index + 1) % 12
    else: break
print(left, dic[curr_index][0])

