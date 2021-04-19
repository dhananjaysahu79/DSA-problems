# maximize profit in buying and selling the stocks with a condition that once
# you buy a stock you have to sell it before buying another one.
# Python 3 solution

arr = list(map(int,input().split()))
curr_stock = arr[0] #variable to store small stock
# mx to store maximum profit at each index for current stock.
# p is the total profit
# prev is used to store previous value of mx.
mx = 0;p = 0;prev = 0
for i in range(1,len(arr)):
    if arr[i] < arr[i-1]: #once we get the element smaller than the previous one we will buy that stock.
        curr_stock = arr[i]
        prev = 0
    else:                   # if the elements continue to be in acsending order
        mx = arr[i] - curr_stock #calculating profit at each index.
        p += mx - prev #subtracting the previous profit from total profit bcoz previous one is no more the maximum profit.
        prev = mx   
print(p)