'''An array contains both positive and negative numbers in random order. 
Rearrange the array elements so that all negative numbers appear before 
all positive numbers.'''

# aplying partiton process  pf quicksort algorithm
def rearrange(arr, n ) :
    # index for the last positive
    j = 0
    for i in range(0, n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    return arr


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
res = rearrange(arr, n)
print(res)

# Time complexity: O(N) 
# Auxiliary Space: O(1)
