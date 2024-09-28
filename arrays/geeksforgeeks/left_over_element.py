'''Given an array arr, the size is reduced by 1 element at each 
step. In the first step, the maximum element would be removed, 
while in the second step, the minimum element of the remaining 
array would be removed, in the third step again the maximum,
 and so on. Continue this till the array contains only one 
 element. And find the final element remaining in the array.'''

def find_left_over(arr: list):
    arr.sort()
    i = 0
    j = len(arr) - 1
   
    if len(arr) == 1:
        return arr[0]
    
    while i <= j:
        if len(arr) == 1:
            return arr[0]
        else:
            
            arr.pop(j)
            print(arr)
            j -= 1
        if len(arr) == 1:
            return arr[0]
        else:
            
            
            arr.pop(i)
            print(arr)
        print(i,j)   
arr = [7, 8, 3, 4, 2, 9, 5]
res = find_left_over(arr)
print(res)