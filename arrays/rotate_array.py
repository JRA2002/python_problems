'''Given an array, the task is to cyclically rotate the array clockwise by one time.'''

def rotate(arr):
    arr[0] = arr[3]
    arr[1] = arr[2]
    arr[2] = arr[1]
    arr[3] = arr[2]

    return arr
arr = [2,3,4,5]
res = rotate(arr)
print(res)