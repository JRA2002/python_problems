'''Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.'''

# withou maintaining order
def move_zeros_end(arr):
    i = 0
    j = 1
    n = len(arr) - 1
    while i <= n and j <= n:
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[i] == 0 and arr[j] == 0:
            j += 1
        else:
            i += 1
            j += 1
        
    return arr

arr = [0,0,0,3,4,5]
res = move_zeros_end(arr)
print(arr)