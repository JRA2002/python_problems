'''Given an m x n matrix, the task is to print all elements of the matrix in spiral form.'''

def spiral(arr):
    
    k = 1
    n = len(arr) - 1 -1
    j = 2 +1
    m = 0-1

    first = arr[k][:n]
    for i in first:
         print(i)
    
    for i in range(k,len(arr) - j):
        last = arr[i][n]
        print(last)
        
    reverse = arr[m - 1][::-1][:m-1]
    print(reverse)
    for i in reverse:
        print(i,'yoyo')
    for i in range(len(arr) - 1, 1, -1):
        first_ele = arr[i][0]
        print(first_ele)  
   






arr= [[1,2,3,4], [5,6,7,8], 
      [9,10,11,12], [13,14,15,16]]

spiral(arr)