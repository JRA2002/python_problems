'''Given an array prices[] of size N denoting the cost of 
stock on each day, the task is to find the maximum total 
profit if we can buy and sell the stocks any number of times.

Note: We can only sell a stock which we have bought earlier 
and we cannot hold multiple stocks on any day.'''

def buy_sell_stocks(arr):
    buy = arr[0]
    win = 0
    sell = 0

    for i in range(len(arr) - 1):
        if arr[i+1] >= arr[i]:
            sell = arr[i+1]  
           
        else:
            if buy < sell:
                win = sell - buy
                print(win)
            buy = arr[i+1]
            
    win = sell - buy
    print(win)
    
arr = [100, 180, 260, 310, 40, 535, 695]
res = buy_sell_stocks(arr)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(1)