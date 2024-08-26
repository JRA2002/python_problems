'''Given an m x n matrix, the task is to print all elements of the matrix in spiral form.'''

def spiral(arr , n, m):
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        
        while right > left:
            for i in range(left,right + 1):
                print(arr[left][i], end=' ')
            top += 1

            for i in range(top,bottom + 1):
                print(arr[i][right], end=' ')
            right -= 1

            for i in range(right, left - 1, -1):
                print(arr[bottom][i],end=' ')
            bottom -= 1
            if bottom >= top:
                for i in range(bottom, left, -1):
                    print(arr[i][left], end=' ')
                left += 1
        
arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

spiral(arr, len(arr), len(arr[0]))

